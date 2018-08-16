from flask import Flask, request, jsonify
import json
import uuid
from api.models import *
from flask import Blueprint


mod = Blueprint('questions', __name__)



@mod.route('/questions', methods=['POST'])
def add_question():
    """
    Function enables user to create a question by first checking if they have
    entered an empty string and returns an error message in that case. If not,
    it creates a question with the information from the json object and adds
    the question to a list of qeustions called 'questions' and returns a
    success message wuth the question that has been created.
    """
    data = request.get_json()

    questionId = len(questions)
    questionId += 1

    details = data.get('details')

    if not details or details.isspace():
        return jsonify({
            "message": "Sorry, you didn't enter any question!"
            }), 400
    question = Question(questionId, details)
    questions.append(question)

    return jsonify({
        "question": question.__dict__,
        "message": "Question added successfully!"
    }), 201
