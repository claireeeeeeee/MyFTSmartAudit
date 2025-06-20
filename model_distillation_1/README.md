# Smart Contract Prompt Project

This project is designed to generate and process prompts for smart contract vulnerability analysis using OpenAI's SDK. You can modify the model to use different models, such GPT, DeepSeek, Gemini, and more. The default model is GPT-4o.

## Structure

- `prompts/`: Initial knowledge.
- `utils/`: Utility scripts for token counting and CSV processing.
- `core/`: Main logic for interacting with OpenAI API.
- `config/`: Configuration settings.
- `data/`: Initial seed knowledge.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Update your API key and CSV file paths in `config/settings.py` and `scripts/main.py`.

```bash
python app.py
```