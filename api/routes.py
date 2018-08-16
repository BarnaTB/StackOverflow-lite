from flask import Flask, request, jsonify
import json
import uuid
# import app
from api.models import *
from flask import Blueprint


mod = Blueprint('questions', __name__)

# app = Flask(__name__)


@mod.route('/questions', methods=['POST'])
def add_question():
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
