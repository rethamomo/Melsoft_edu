

# Education site

This is a Flask-based web application for managing courses, assignments, and profiles.

## Prerequisites

- Python 3.10
- `venv` module for creating virtual environments

## Installation



1. Create a virtual environment:
    
    python3 -m venv venv
    

2. Activate the virtual environment:
    - On Linux or macOS:
        
        source venv/bin/activate
        
    - On Windows:
        
        .\venv\Scripts\activate
        

3. Install the required packages:
    
    pip install -r requirements.txt
    

## Running the Application

1. Ensure the virtual environment is activated.
2. Run the Flask application:
    
    python main.py
    

3. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.



## Updating Dependencies

To update the `requirements.txt` file with new dependencies, follow these steps:

1. Install the new package using `pip`:
    ```
    pip install <package-name>
    ```

2. Freeze the current environment's dependencies to `requirements.txt`:
    ```
    pip freeze > requirements.txt
    ```


## Project Structure

- `main.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing static files like CSS.
- `requirements.txt`: File listing the required Python packages.


