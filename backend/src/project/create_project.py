from utils import generate_response
from project.prompts import project_description_prompt, project_fields_extract_prompt, project_fields_predict_prompt
import concurrent.futures
import re

def get_detailed_project_description(description):
    prompts = project_description_prompt(description)

    # prompts = project_prompts.project_description_prompt(
    #     project_heading=project_heading,
    #     project_description=project_description,
    #     skills_required=skills_required,
    #     project_duration=project_duration,
    #     budget=budget
    # )

    # print(prompts['system_prompt'], prompts['user_prompt'])
    response = generate_response(prompts['system_prompt'], prompts['user_prompt'])
    return response

def extract_project_fields(description):
    fields = ['Project name', 'Skills required', 'Estimated budget', 'Estimated project duration']
    prompts = project_fields_extract_prompt(description, fields)
    # print(prompts['system_prompt'], prompts['user_prompt'])
    response = generate_response(prompts['system_prompt'], prompts['user_prompt'])
    # print(response)
    result = _parse_raw_fields(response, fields)
    return result

def suggest_project_fields(description):
    fields = ['Project name', 'Skills required', 'Estimated budget', 'Estimated project duration']
    prompts = project_fields_predict_prompt(description, fields)
    # print(prompts['system_prompt'], prompts['user_prompt'])
    response = generate_response(prompts['system_prompt'], prompts['user_prompt'])
    # print(response)
    result = _parse_raw_fields(response, fields)
    return result

def _parse_raw_fields(text, fields):
    # parse fields from text
    field_results = {}
    for field in fields:
        match = re.search(f"{field}:(.*)", text, re.IGNORECASE)
        if match:
            field_results[field] = match.group(1).strip()
        else:
            field_results[field] = None

    return field_results

def fire_and_forget(description):
    # list of function calls
    function_calls = [
        get_detailed_project_description, 
        extract_project_fields, 
        suggest_project_fields
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(function_calls)) as executor:
        # Submit API calls asynchronously
        futures = [executor.submit(function, description) for function in function_calls]
        
        # Wait for all futures to complete
        concurrent.futures.wait(futures)
        
        results = {}
        # suggested_description
        results['suggested_description'] = futures[0].result()
        # extracted_fields
        results['extracted_fields'] = futures[1].result()
        # suggested_fields
        results['suggested_fields'] = futures[2].result()
        return results

def process_project_description(description):
    results = fire_and_forget(description)
    return results
