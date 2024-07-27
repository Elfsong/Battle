# Coding: utf-8

# Author: Mingzhe Du (mingzhe@nus.edu.sg)
# Date: 2024 / 07 / 26

import utils
import torch
import transformers
from openai import OpenAI

class GPTAgent():
    def __init__(self, model_name, api_key) -> None:
        self.model_name = model_name
        self.api_key = api_key
        
        self.client = OpenAI(api_key=api_key)
        
    def prompt_generation(self, problem_description):
        prompt = utils.few_shot_prompt + "\n" + problem_description
        return prompt
    
    def code_generation(self, prompt) -> str:
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a coding export. You response in Pure Python code only (explicitly import all libraries). Consider each input is a string, so use 'eval' to parse these inputs, and use * to decouple arguments."},
                {"role": "user", "content": prompt}
            ],
        )

        return completion.choices[0].message.content

class DeepSeekAgent():
    def __init__(self, model_name, api_key) -> None:
        self.model_name = model_name
        self.api_key = api_key
        
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        
    def prompt_generation(self, problem_description):
        prompt = utils.few_shot_prompt + "\n" + problem_description
        return prompt
    
    def code_generation(self, prompt) -> str:
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a coding export. You response in Pure Python code only (explicitly import all libraries). Consider each input is a string, so use 'eval' to parse these inputs, and use * to decouple arguments."},
                {"role": "user", "content": prompt}
            ],
        )

        return completion.choices[0].message.content
    
class HuggingFaceAgent():
    def __init__(self, model_name, api_key) -> None:
        self.model_name = model_name
        self.api_key = api_key
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_name,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map="auto",
        )
        
    def prompt_generation(self, problem_description):
        prompt = utils.few_shot_prompt + "\n" + problem_description
        return prompt

    def code_generation(self, prompt) -> str:
        messages = [
            {"role": "system", "content": "You are a coding export. You response in Pure Python code only (explicitly import all libraries). Consider each input is a string, so use 'eval' to parse these inputs, and use * to decouple arguments."},
            {"role": "user", "content": prompt},
        ]

        outputs = self.pipeline(
            messages,
            max_new_tokens=2048,
        )
        
        return outputs[0]["generated_text"][-1]
