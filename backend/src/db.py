import ast
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from freelancer.prompts import get_top_freelancers_prompt
from project.prompts import get_top_projects_prompt
from utils import generate_response

class FirebaseDB:
    def __init__(self):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('../data/indilancer-c9297-firebase-adminsdk-cww8c-9095e5319a.json')

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://indilancer-c9297-default-rtdb.firebaseio.com/'
        })

        # As an admin, the app has access to read and write all data, regradless of Security Rules
        self.ref = db.reference('/')

    def get_tables(self):
        return list(self.ref.get().keys())

    def get_freelancers(self, project_obj):
        skill = project_obj['aiProjSkills'].split(',')[0]
        all_users = self.ref.get()['users']
        freelancers = [all_users[user] for user in all_users if all_users[user].get('userType') == 'FREELANCER']
        # print("freelancers", freelancers)

        # filter freelancers by skill
        result = []
        for freelancer in freelancers:
            print(freelancer.get('userSkillSet', []))
            if skill in freelancer.get('userSkillSet', []):
                result.append(freelancer)
        # print("Matched freelancers", result)

        # get top freelancers
        project_obj.pop('projDesc')
        prompt = get_top_freelancers_prompt(project_obj, result)
        # print(prompt['system_prompt'], prompt['user_prompt'])
        top_freelancers_indices = generate_response(prompt['system_prompt'], prompt['user_prompt'])
        # print(top_freelancers_indices)
        top_freelancers_indices = ast.literal_eval(f"'{top_freelancers_indices}'")
        # print(type(top_freelancers_indices), top_freelancers_indices)
        # get the top projects in order of top_project_indices
        if not isinstance(top_freelancers_indices, list) or len(top_freelancers_indices) == 0:
            top_freelancers = freelancers[:5]
        else:
            top_freelancers = [result[index-1] for index in top_freelancers_indices]

        return top_freelancers
    
    def get_projects(self, freelancer_obj):
        skill = freelancer_obj['userSkillSet'].split(',')[0]
        all_projects = self.ref.get()['allProjects']
        all_projects = [all_projects[project] for project in all_projects]
        # print("all_projects", all_projects)
        # print("skill", skill)

        result = []
        for project in all_projects:
            # print(project.get('aiProjSkills', []))
            if skill in project.get('aiProjSkills', []):
                result.append(project)
        # print("Matched projects", result)

        # get top projects
        prompt = get_top_projects_prompt(freelancer_obj, result)
        # print(prompt['system_prompt'], prompt['user_prompt'])
        top_project_indices = generate_response(prompt['system_prompt'], prompt['user_prompt'])
        # print(top_project_indices)
        top_project_indices = ast.literal_eval(top_project_indices)
        # get the top projects in order of top_project_indices
        top_projects = [result[index-1] for index in top_project_indices]
        
        return top_projects

