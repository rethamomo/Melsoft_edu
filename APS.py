import google.generativeai as genai
from flask import request
import os
import tempfile

# Configure the Gemini model
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Load the Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def calculate_APS_score():
    # Get the uploaded file from the Flask request
    report_file = request.files.get('report')  # Safely access the file
    
    # Check if a file is uploaded
    if report_file and report_file.filename != '':
        try:
            # Save the file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                report_file.save(tmp.name)
                temp_file_path = tmp.name

            # Upload the file to the Gemini API
            uploaded_file = genai.upload_file(temp_file_path)
            print(75,uploaded_file,73,temp_file_path)

            
            file_uri = uploaded_file['uri']  # Extract the URI from the uploaded file metadata
            print(file_uri)


            # Create a prompt for Gemini
            prompt = "From the report card content, calculate the APS and provide a breakdown of the calculation for a South African student.\n\n"
            # Send the prompt along with the uploaded file content to the Gemini API for content generation
            # rog=model.generate_content("how many sheep do americans own")
            response = model.generate_content([prompt,uploaded_file])
            print("haw")
            
            # Return the response content if available
            return response.text
            # return rog.text

        except Exception as e:
            # Handle any exceptions and return a generic error message
            return 'An error occurred while processing the file.'
    else:
        # Return an error message if no file is uploaded
        return 'No file uploaded or invalid file format.'
