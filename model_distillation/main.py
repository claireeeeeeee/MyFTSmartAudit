import os
from core.process_seeds import process_seeds_csv
from config import settings  # 这里假设 settings.py 也在 model_distillation/config/

if __name__ == "__main__":
    # ✅ 设置你的 seed 合约 CSV 路径
    csv_path = "/Users/cli776/Documents/FTSmartAudit/model_distillation/data/sample_seed_knowledge_v2.csv"  # 建议你把种子 CSV 放到 model_distillation/data/ 目录下

    # ✅ 读取你的配置文件（API key、模型、温度等）
    api_key = settings.API_KEY
    input_types = settings.INPUT_TYPES
    type_descriptions = settings.TYPE_DESCRIPTIONS
    temperatures = settings.TEMPERATURES
    model = settings.MODELS

    # ✅ 调用种子处理函数，批量生成 Prompt
    process_seeds_csv(
        csv_path=csv_path,
        api_key=api_key,
        input_types=input_types,
        type_descriptions=type_descriptions,
        temperatures=temperatures,
        model=model
    )
