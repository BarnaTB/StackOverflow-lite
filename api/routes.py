from flask import Flask, request, jsonify
import json
import uuid
from api import app
from api.models import *


@app.route('/questions', method=['POST'])
def add_question():
    data = request.get_json()

    questionId = len(questions)
    questionId += 1

    question_id = data.get('questionId')
    details = data.get('details')

    if not details and len(details.strip(" ")) != 0:
        return jsonify({"message": "Please enter question details"}), 400
    question = Question(question_id, details)
    questions.append(question)

    return jsonify({
        "question": question.__dict__,
        "message": "Question added successfully!"
    }), 201


@app.route('/questions/<questionId>/answers', method=['POST'])
def add_answer(questionId: int):
    data = request.get_json()

    questionId = data.get('questionId')
    details = data.get('details')

    if not details and len(details.strip(" ")) != 0:
        return jsonify({'message': 'Please enter an answer.'}), 400
    if questionId > len(questions) or questionId <= len(questions):
        return jsonify({'message': 'Question does not exist!'}), 400
    answer = Answer(questionId, details)
    answers.append(answer)

    return jsonify({
        'Answer': 
    })
