# IndiLancer
The "Nexties" have developed a platform that empowers freelancers and employers to connect throught the power of AI

## Unique Value Proposition (UVP)
-	Use AI to match freelancers with employers
-	Create job post in minutes not hours
-	Use natural language processing to interpret project descriptions and extract key requirements for more accurate matching.

## Repo structure
The repo is divided into the frontend and backend code. The frontend has been developed as an Android application written in Java. The backend in written in Python which hosts the APIs required by the frontend.

## Get started
1. Clone the repo

   ```
   git clone https://github.com/coder-shubham/Nexties-IndiLancer-HackBangalore.git
   cd Nexties-IndiLancer-HackBangalore/backend
   ```

2. Create a virtual environment using your favourite python version >= 3.7 and install the dependencies

   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Export an environment variable with your openai key

   ```
   export OPENAI_API_KEY=<YOUR_KEY_GOES_HERE>
   ```

4. Get a hold of the credentials for a service account for your project, you'll need to generate one from the Firebase console from `Project Settings -> Service Accounts`. The documentation is [here](https://firebase.google.com/docs/admin/setup#add_firebase_to_your_app)
   
5. Start the backend Flask server

   ```
   cd src/
   python app.py
   ```

   The application will start running locally on port 5000.

6. Download and install the Android app from the release section.

   That's it!
