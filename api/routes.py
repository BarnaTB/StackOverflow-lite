from flask import Flask, request, jsonify
import json
import uuid
from api import app
from api.models import *


@app.route('/questions', method=['POST'])
def add_question():
    data = request.get_json()

    question_id = len(questions)
    question_id += 1

    question_id = data.get('question_id')
    details = data.get('details')

    if not details and len(details.strip(" ")) != 0:
        return jsonify({"message": "Please enter question details"}), 400
    question = Question(question_id, details)
    questions.append(question)

    return jsonify({
        "question": question.__dict__,
        "message": "Question added successfully!"
    }), 201
