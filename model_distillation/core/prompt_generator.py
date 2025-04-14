from openai import OpenAI
import time
from typing import List

class SmartContractPromptGenerator:
    def __init__(self, api_key: str):
        """
        Initialize with OpenAI API key.
        """
        self.client = OpenAI(api_key=api_key)

    def _create_system_message(self) -> str:
        return (
            "You are an expert in prompt engineering and smart contract analysis. "
            "You will generate a complete and effective data generation prompt for a teacher model "
            "based on a given smart contract vulnerability analysis template and contract type."
        )

    def _create_user_message(self, seed_knowledge: str, input_type: str, type_description: str) -> str:
        return f"""You are provided with a piece of seed knowledge, including a Solidity smart contract and its vulnerability analysis.

        Your task is to generate a new prompt for a teacher model. This prompt must guide the teacher model to:

        1. Generate a new Solidity smart contract that belongs to the following category:  
        - **Contract Type**: {input_type}  
        - **Category Description**: {type_description}
        2. Ensure the generated smart contract includes **at least two vulnerabilities** present in the seed knowledge.
        3. Output the results using **only** the following format, with no additional explanations or text outside the structure:

        ```markdown
        ### Instruction:
        List all the vulnerabilities in the following Solidity code of a smart contract:

        ### Input:
        ```solidity
        // Your generated Solidity smart contract code for the specified {input_type}
        ```

        ### Response:
        Identified vulnerabilities:
        1. **Vulnerability Name** *(Severity Level)*:  
        **Description:**  
        [Clear technical explanation of vulnerability]
        
        **Impact:**  
        [Potential consequences if exploited]

        **Mitigation:**  
        ```solidity
        // Specific code changes to fix
        ```

        ...(additional vulnerabilities if present)
        ```

        Here is the seed knowledge:
        ```
        {seed_knowledge}
        ```

        Generate and return the full teacher model prompt that adheres strictly to this format."""

    def _generate_prompt_with_retries(
        self,
        seed_knowledge: str,
        input_type: str,
        type_description: str,
        model: str,
        temperature: float,
        max_retries: int,
        retry_delay: float
    ) -> str:
        messages = [
            {"role": "system", "content": self._create_system_message()},
            {"role": "user", "content": self._create_user_message(seed_knowledge, input_type, type_description)}
        ]

        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=temperature
                )
                prompt = response.choices[0].message.content.strip()
                if prompt:
                    return prompt
            except Exception as e:
                if attempt == max_retries - 1:
                    raise Exception(f"Failed to generate prompt: {str(e)}")
                time.sleep(retry_delay)
        raise Exception("Failed to generate a valid prompt.")

    def generate_teacher_prompts(
        self,
        seed_knowledge: str,
        input_type: str,
        type_description: str,
        num_prompts: int = 3,
        model: str = "gpt-4o",
        temperature: float = 0.7,
        max_retries: int = 3,
        retry_delay: float = 1.0
    ) -> List[str]:
        """
        Generate multiple teacher prompts based on input seed knowledge and contract type.

        Args:
            seed_knowledge (str): Example contract and vulnerability analysis to guide generation.
            input_type (str): Type/category of the contract (e.g., "Token Contract").
            type_description (str): Description of the contract category.
            num_prompts (int): Number of prompts to generate.
            model (str): OpenAI model to use (default: "gpt-4o").
            temperature (float): Sampling temperature (controls creativity).
            max_retries (int): Max retries for failed API calls.
            retry_delay (float): Delay in seconds between retries.

        Returns:
            List[str]: A list of generated prompts.
        """
        prompts = []
        for _ in range(num_prompts):
            prompt = self._generate_prompt_with_retries(
                seed_knowledge=seed_knowledge,
                input_type=input_type,
                type_description=type_description,
                model=model,
                temperature=temperature,
                max_retries=max_retries,
                retry_delay=retry_delay
            )
            prompts.append(prompt)
            time.sleep(5)  # To respect rate limits
        return prompts

def generate_smart_contract_prompts(
    seed_knowledge: str,
    input_type: str,
    type_description: str,
    num_prompts: int,
    api_key: str,
    temperature: float,
    model: str = "gpt-4o"
) -> List[str]:
    """
    High-level wrapper for generating smart contract prompts.

    Args:
        seed_knowledge (str): Seed example for guidance.
        input_type (str): Contract type (e.g., "Token Contract").
        type_description (str): Brief description of the contract type.
        num_prompts (int): How many prompts to generate.
        api_key (str): OpenAI API key.
        temperature (float): Temperature for sampling (creativity).
        model (str): Model to use (default: "gpt-4o").

    Returns:
        List[str]: Generated teacher prompts.
    """
    generator = SmartContractPromptGenerator(api_key)
    return generator.generate_teacher_prompts(
        seed_knowledge=seed_knowledge,
        input_type=input_type,
        type_description=type_description,
        num_prompts=num_prompts,
        model=model,
        temperature=temperature
    )