from flask import Flask, request, jsonify
import json
import uuid
from api.utilities import *
from api.models import *
from flask import Blueprint


mod = Blueprint('answers', __name__)


@mod.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()

    questionId = len(questions)
    questionId += 1

    details = data.get('details')

    if not details or details.isspace():
        return jsonify({"message": "Missing question!"}), 400
    question = Question(questionId, details)
    questions.append(question)

    return jsonify({
        "question": question.__dict__,
        "message": "Question added successfully!"
    }), 201


@mod.route('/questions/<int:questionId>/answers', methods=['POST'])
def add_answer(questionId):
    data = request.get_json()

    details = data.get('details')

    # try:
    if not details or details.isspace():
        return jsonify({
            'message': 'Sorry, you did not enter any answer!'
            }), 400
    if len(questions) == 0:
        return jsonify({
            'message': 'Sorry, there are no questions yet!!'
            }), 400
    question = get_question(questionId)
    answer = Answer(question, details)
    answers.append(answer)

    return jsonify({
        'questionId': questionId,
        'Answer': answer.__dict__,
        'Message': 'Answer added succesfully!'
    }), 201
    # except TypeError:
        # return jsonify({
        #     'message': 'question id must be a number!'
        # }), 400
