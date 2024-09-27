import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def greet_user():
    greeting = model.generate_content("Do not give me direct answers just push me in the right direction")
    return greeting

def make_request(subject, proficiency, question):
    
    response = model.generate_content("explain this " + subject + " to me at this proficiency " + proficiency + ": " + question)
    return response.text