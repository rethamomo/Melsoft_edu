import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

conversation_history = []

def greet_user():
    greeting = model.generate_content("Do not give me direct answers just push me in the right direction")
    conversation_history.append({"role": "system", "content": greeting.text})
    return greeting.text

# def make_request(subject, proficiency, question):
#     conversation_history.append({"role": "user", "content": f"explain this {subject} to me at this proficiency {proficiency}: {question}"})
    
#     response = model.generate_content(conversation_history[-1])
#     conversation_history.append({"role": "assistant", "content": response.text})
    
#     return response.text

def make_request(subject, proficiency, question):
    
    response = model.generate_content("explain this " + subject + " to me at this proficiency " + proficiency + ": " + question)
    return response.text

def communicate_with_gemini(user_input, conversation_history=[]):
    # Maintain the conversation context by adding previous history
    conversation_history.append(user_input)  # Add the latest user input to the conversation

    # Create a conversation prompt
    prompt = "\n".join(conversation_history)  # Join all previous inputs and responses

    # Send the prompt to the Gemini model and get the response
    response = model.generate_content([prompt])

    # Get the text from the Gemini response
    gemini_response = response.text

    # Add the response to the conversation history
    conversation_history.append(gemini_response)

    # Return the latest response from Gemini
    return gemini_response, conversation_history