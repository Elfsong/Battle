# Coding: utf-8

# Author: Mingzhe Du (mingzhe@nus.edu.sg)
# Date: 2024 / 07 / 26

import os
import utils
import agents
from tqdm import tqdm
from codearena import codearena

arena_client = codearena.CodeArena(url_root='https://codearena.online', token=os.getenv('CODEARENA_API_KEY'))
# model_client = agents.GPTAgent(model_name='gpt-3.5-turbo', api_key=os.getenv('OPENAI_API_KEY'))
model_client = agents.DeepSeekAgent(model_name='deepseek-coder', api_key=os.getenv('DEEPSEEK_API_KEY'))

# Get problem list
problems = arena_client.get_problems()
problems = problems['data']['objects']

# Solution Process
for problem_info in tqdm(problems):
    # print(problem_info)
    problem_code= problem_info['code']
    problem = arena_client.get_problem(problem_id=problem_code)['data']['object']
    problem_description = problem['description']
    
    prompt = model_client.prompt_generation(problem_description)
    solution = model_client.code_generation(prompt)
    code_solution = utils.code_match(solution)
    code_solution = code_solution[0] if code_solution else solution    
    submission_result = arena_client.post_submission(problem_id=problem_code, language="Python 3", source=code_solution)
    # print(submission_result)


