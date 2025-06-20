from core.process_seeds import process_seeds_csv
from config.settings import API_KEY, INPUT_TYPES, TYPE_DESCRIPTIONS, TEMPERATURES, MODELS

if __name__ == "__main__":
    process_seeds_csv(
        csv_path="./data/sample_seed_knowledge_v2.csv",
        api_key=API_KEY,
        input_types=INPUT_TYPES,
        type_descriptions=TYPE_DESCRIPTIONS,
        temperatures=TEMPERATURES,
        model= MODELS
    )
