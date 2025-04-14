import time
from datetime import timedelta
import pandas as pd
from typing import List
from core.prompt_generator import generate_smart_contract_prompts
from utils.token_counter import count_tokens

def process_seeds_csv(
    csv_path: str,
    api_key: str,
    input_types: List[str],
    type_descriptions: List[str],
    temperatures: List[float],
    model: str = "gpt-4o-2024-11-20"
):
    """
    Processes each row in the CSV with real-time monitoring and timing
    """
    if len(input_types) != len(type_descriptions):
        raise ValueError("input_types and type_descriptions must be equal length.")

    # Load CSV and initialize tracking
    df = pd.read_csv(csv_path)
    start_time = time.time()
    processed = 0
    skipped = 0
    failed = 0
    iteration_counter = 0
    
    print(f"🚀 Starting processing of {len(df)} seed contracts")
    print(f"📊 Will generate {len(df)*len(input_types)*len(temperatures)} total combinations")

    for i, row in enumerate(df.iterrows()):
        _, row_data = row
        seed = row_data['Seed']
        
        for input_type, description in zip(input_types, type_descriptions):
            for temp in temperatures:
                iteration_counter += 1
                iter_start = time.time()
                
                # Rate limiting
                if iteration_counter % 10 == 0:
                    time.sleep(0.03)  # 30ms delay
                    
                # Skip check
                if ((df['Seed'] == seed) & 
                    (df['input_type'] == input_type) & 
                    (df['temperature'] == temp)).any():
                    skipped += 1
                    print(f"⏭️ [{i+1}/{len(df)}] Skipped existing: {input_type}@{temp}")
                    continue

                try:
                    # Generate with timing
                    gen_start = time.time()
                    generated = generate_smart_contract_prompts(
                        seed_knowledge=seed,
                        input_type=input_type,
                        type_description=description,
                        num_prompts=1,
                        api_key=api_key,
                        temperature=temp,
                        model=model
                    )
                    gen_time = time.time() - gen_start

                    # Create new row
                    new_row = pd.DataFrame([{
                        'Seed': seed,
                        'contract_seed': generated[0],
                        'temperature': temp,
                        'input_type': input_type,
                        'type_description': description,
                        'model': model,
                        'tokens': count_tokens(generated[0], model=model)
                    }])

                    # Save and track
                    df = pd.concat([df, new_row], ignore_index=True)
                    df.to_csv(csv_path, index=False)
                    
                    processed += 1
                    iter_time = time.time() - iter_start
                    print(
                        f"✅ [{i+1}/{len(df)}] Added {input_type}@{temp} "
                        f"(Gen: {gen_time:.1f}s, Total: {iter_time:.1f}s) "
                        f"Tokens: {new_row['tokens'].values[0]}"
                    )

                except Exception as e:
                    failed += 1
                    print(f"❌ [{i+1}/{len(df)}] Failed {input_type}@{temp}: {str(e)[:50]}...")
                    continue

    # Final report
    total_time = timedelta(seconds=time.time()-start_time)
    print(f"\n🎉 Processing complete in {total_time}")
    print(f"• Processed: {processed}")
    print(f"• Skipped: {skipped}")
    print(f"• Failed: {failed}")
    print(f"• Final CSV size: {len(df)} rows")
    
    return df