from flask import Flask, request, jsonify

from utils import generate_response
from project.create_project import process_project_description
from freelancer.create_profile import ResumeReader
from db import FirebaseDB

app = Flask(__name__)

fire_db = FirebaseDB()

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

# login
# @app.route('/freelancer/login', methods=['POST'])

# profile

# create
@app.route('/freelancer/profile/create', methods=['POST'])
def set_profile_details():
    data = request.get_json()
    # authenticate token
    token = data['auth_token']

    # get user profile details
    username = data['username']
    email = data['email']
    skills = data['skills']
    experience = data['experience']

    # upload to db

    return jsonify({"message": "Profile created successfully"})

# view
@app.route('/freelancer/profile/view', methods=['POST'])
def get_profile_details():
    data = request.get_json()
    # authenticate token
    token = data['auth_token']

    # get user id
    user_id = data['user_id']
    
    # get user profile details from db

    dummy_data = {
        "username": "John Doe",
        "email": "john@example.com",
        "skills": ["Python", "Java", "C++"],
        "experience": "2 years"
    }
    return jsonify(dummy_data)

# resume parser
@app.route('/freelancer/parse_resume', methods=['POST'])
def parse_resume():
    # data = request.get_json()
    # authenticate token
    # token = request.form.get('auth_token')

    # get resume file
    resume_file = request.files.get('resume_file')
    
    # parse resume
    resume = ResumeReader(resume_file)
    resume.extract_text_from_pdf()
    fields = resume.get_fields()

    return jsonify(fields)

@app.route('/employer/suggest/freelancers', methods=['POST'])
def suggest_freelancers():
    data = request.get_json()
    # authenticate token
    # token = data['auth_token']

    # get user id
    # user_id = data['user_id']
    project_obj = data['project']

    result = fire_db.get_freelancers(project_obj)
    output = {
        "suggested_freelancers": result
    }
    
    # get user profile details from db
    return jsonify(output)

# project

# create
@app.route('/project/create', methods=['POST'])
def create_project():
    data = request.get_json()
    # authenticate token
    token = data['auth_token']

    # get project details
    project_name = data['project_name']
    project_description = data['project_description']
    skills_required = data['skills_required']
    project_duration = data['project_duration']

    # upload to db

    return jsonify({"message": "Project created successfully"})

# view
@app.route('/project/view', methods=['POST'])
def view_project():
    data = request.get_json()
    # authenticate token
    token = data['auth_token']

    # get project id
    project_id = data['project_id']
    
    # get project details from db

    dummy_data = {
        "project_name": "Project X",
        "project_description": "This is a dummy project",
        "skills_required": ["Python", "Java", "C++"],
        "project_duration": "2 months"
    }
    return jsonify(dummy_data)

# ai builder
@app.route('/project/suggest/description', methods=['POST'])
def suggest_project_description():
    data = request.get_json()
    # authenticate token
    # token = data['auth_token']

    # get project name
    # project_heading = data['project_heading']
    project_description = data['project_description']
    # skills_required = data['skills_required']
    # project_duration = data['project_duration']
    # budget = data['budget']

    # generate project description using AI
    response = process_project_description(project_description)

    return jsonify(response)

@app.route('/freelancer/suggest/projects', methods=['POST'])
def suggest_projects():
    data = request.get_json()
    # authenticate token
    # token = data['auth_token']

    # get user id
    # user_id = data['user_id']
    freelancer_obj = data['user']

    result = fire_db.get_projects(freelancer_obj)
    output = {
        "suggested_projects": result
    }
    
    # get user profile details from db
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)