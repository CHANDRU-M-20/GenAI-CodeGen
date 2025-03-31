from flask import Flask, render_template, request,jsonify
from model import LLM
from pathlib import Path
from dotenv import load_dotenv
import os
app = Flask(__name__)


@app.route('/')
def home():
    return {
        "message": "Welcome to the Flask app!"
    }

@app.route('/query', methods=['GET'])
def llm():
    query = request.json.get('query')
    print(query)
    model = LLM("gemini-1.5-pro")
    llm = model.get_llm()
    print("LLM initialized successfully.")  
    response = llm.invoke(query)
    with open("response.txt", "w") as file:
        file.write(response.content)
    return jsonify({"response": response.content})
    
@app.route('/history', methods=['GET'])    
def get_history_data():
    with open("response.txt","r") as file:
        history = file.read()
    return {
        "history": history
    }
    


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")