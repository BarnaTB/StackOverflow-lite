from flask import Flask, request, jsonify
import json
import uuid
from api import app
from api.models import *


@app.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()

    questionId = len(questions)
    questionId += 1

    question_id = data.get('questionId')
    details = data.get('details')

    if not details and len(details.strip(" ")) != 0:
        return jsonify({"message": "Missing question!"}), 400
    question = Question(question_id, details)
    questions.append(question)

    return jsonify({
        "question": question.__dict__,
        "message": "Question added successfully!"
    }), 201


@app.route('/questions/<questionId>/answers', methods=['POST'])
def add_answer(questionId: int):
    data = request.get_json()

    questionId = data.get('questionId')
    details = data.get('details')

    try:
        if not details and len(details.strip(" ")) != 0:
            return jsonify({'message': 'Please enter an answer.'}), 400
        if questionId > len(questions) or questionId <= 0:
            return jsonify({'message': 'Question does not exist!'}), 400
        answer = Answer(questionId, details)
        answers.append(answer)

        return jsonify({
            'Answer': answer.__dict__,
            'Message': 'Answer added succesfully!'
        }), 201
    except TypeError:
        return jsonify({
            'message': 'question id must be a number!'
        }), 400
