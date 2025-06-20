import pandas as pd
import re

def process_content(content):
    if pd.isna(content):
        return content
    content = re.sub(r'^```markdown\s*', '', str(content), count=1)
    content = re.sub(r'\s*```$', '', content, count=1)
    return content.strip()


def process_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    df['contract_seed'] = df['contract_seed'].apply(process_content)
    df.to_csv(output_file, index=False)


def delete_rows(input_file, output_file, start_row=0, end_row=133):
    df = pd.read_csv(input_file)
    df.drop(index=range(start_row, end_row + 1), inplace=True)
    df.to_csv(output_file, index=False)


def combine_csv_files(file1_path, file2_path, output_path, skip_header=False):
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path, header=0 if not skip_header else None)
    combined_df = pd.concat([df1, df2], ignore_index=True)
    combined_df.to_csv(output_path, index=False)
