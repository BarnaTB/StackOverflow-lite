from flask import Flask, request, jsonify
import json
import uuid
from api.utilities import *
from api.models import *
from flask import Blueprint


mod = Blueprint('answers', __name__)


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
        return jsonify({"message": "Missing question!"}), 400
    question = Question(questionId, details)
    questions.append(question)

    return jsonify({
        "question": question.__dict__,
        "message": "Question added successfully!"
    }), 201


@mod.route('/questions/<int:questionId>/answers', methods=['POST'])
def add_answer(questionId):
    """
    Function enables user to add an answer to a question on the platform.
    Checks if there is an empty string and returns a message telling the
    user that they didn't enter anything. Also checks if there are any
    questions in the list and if not returns a message that there are not
    questions yet.
    Then checks if the question whose id they entered exists and if not,
    returns a message that the quetion does not exist else, returns the
    answer the user entered together with the question.

    :param questionId:
    Parameter holds the id of the question that the user wishes to answer.
    """
    data = request.get_json()

    details = data.get('details')

    try:
        if not details or details.isspace():
            return jsonify({
                'message': 'Sorry, you did not enter any answer!'
            }), 400
        if len(questions) == 0:
            return jsonify({
                'message': 'Sorry, there are no questions yet!!'
            }), 400

        question = questions[questionId - 1]
        answer = Answer(questionId, details)
        answers.append(answer)

        return jsonify({
            'Question': question.__dict__,
            'Answer': answer.__dict__,
            'Message': 'Answer added succesfully!'
        }), 201
    except IndexError:
        return jsonify({
            'message': 'Question does not exist.'
        }), 400
