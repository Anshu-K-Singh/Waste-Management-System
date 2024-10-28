# Waste Management System 
 to see the live webapp : [here](https://waste-management-system-6rkg.onrender.com) 

### Installation

1. **Clone the repository:**
   ```bash
   git clone repo_name
   ```
2. **Navigate to the project directory:**
   ```bash
   cd into the root folder
   ```
3. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Linux/macOS
   env\Scripts\activate  # On Windows
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```


### Running the App

1. **Initialize the database:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
2. **Run the Flask app:**
   ```bash
   python app.py
   ```
   - The app will be accessible at `http://127.0.0.1:5000/`.
