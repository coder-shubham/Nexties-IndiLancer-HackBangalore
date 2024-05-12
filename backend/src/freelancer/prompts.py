def get_profile_fields_extraction_prompt(text, fields):
    separator = "\n"
    return {
        "system_prompt": """You are an expert in natural language processing and deciphering complex information.""",
        "user_prompt": f"""Extract the following fields from the resume text:\n{separator.join(fields)}\n\nNote:\n- Extract all fields.\n- Do not use bullet points.\n- Fact check all values.\n- If any field is not present, return None for that field.\n- Experience should be a numerical value in years (Eg. 5 years, 8 years, etc.).\n- If a field's value is more than a single line, summarize it striclty in a single line.\n- Output in plain text format.\n\nHere is the resume:\n{text}"""
    }

def get_top_freelancers_prompt(project_obj, freelancers_list):
    separator = "\n"
    return {
        "system_prompt": """You are a project manager looking to hire freelancers for a project.""",
        "user_prompt": f"""Based on the project description given below, suggest the indices of top 5 freelancers who would be the best fit for the project. Provide the indices of the top candidates in a list. If no freelancers are given, return an empty list.\n\nProject Description:\n{project_obj}\n\nFreelancers:\n{separator.join(f'{i+1}: {freelancer}' for i, freelancer in enumerate(freelancers_list))}"""
    }

# "user_prompt": f"""Extract the following information from the resume text:\n{separator.join(fields)}\n\nNote:\n- Extract all fields.\n- If any field is not present, return None for that field.\n\nHere is the resume:\n{text}"""

# "user_prompt": f"""Extract the following information from the resume text:\n{separator.join(fields)}\n\nNote:\n- Extract all the given fields.\n- Keep the values of a particular field strictly in a single line and on the same line as the field name (Eg: Field name: Field value).\n- If any field is not present, return None for that field.\n\nHere is the resume:\n{text}"""