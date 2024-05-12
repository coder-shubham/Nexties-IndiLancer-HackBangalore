# def project_description_prompt(project_heading, project_description, skills_required, 
#                                project_duration, budget):
#     return {
#         "system_prompt": """You are an expert in project management. You will create a description for a project based on the details given by the user.""",
#         "user_prompt": f"""Create a detailed project description based on the following information:\n\nTopic: {project_heading}\nDescription: {project_description}\nSkills Required: {skills_required}\nDuration: {project_duration}\nBudget: {budget}""",
#     }

def project_description_prompt(project_description):
    return {
        "system_prompt": """You are an expert project manager.""",
        "user_prompt": f"""Create a detailed project description in a list format. Do not have sections, but put everything as bullet points. Here is the project description:\n{project_description}""",
    }

def project_fields_extract_prompt(project_description, fields):
    separator = "\n"
    return {
        "system_prompt": """You are an expert project consultant.""",
        "user_prompt": f"""Extract the following information from the project description:\n{separator.join(fields)}\n\nNote:\n- Extract all mentioned fields.\n- Stick to extraction only from given description, do not make your own answers.\n- If any field is missing, return '' an empty string for that field.\n\nHere is the project description:\n{project_description}"""
    }

def project_fields_predict_prompt(project_description, fields):
    separator = "\n"
    return {
        "system_prompt": """You are an expert project consultant.""",
        "user_prompt": f"""Predict the following information from the given project description:\n{separator.join(fields)}\n\n- Even if some value is given in the description, suggest a value based on historical data for such field based on the given description without asking for further clarifications.\n- Predict all fields.\n- The skills here refer to the technical skills required (eg. C++, SQL, Machine Learning, etc.)\n\nHere is the project description:\n{project_description}"""
    }

def get_top_projects_prompt(freelancer_obj, projects_list):
    separator = "\n"
    return {
        "system_prompt": """You are a freelancer looking to work on a project.""",
        "user_prompt": f"""Based on the freelancer profile given below, suggest the indices of top 5 projects from given list which would be the best fit for the freelancer. Provide the indeices of the top projects in a list. Don't be verbose.\n\nFreelancer profile:\n{freelancer_obj}\n\nProjects:\n{separator.join(f'{i+1}: {project}' for i, project in enumerate(projects_list))}"""
    }