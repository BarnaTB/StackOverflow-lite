from flask import Flask, request, jsonify
import json
import uuid
# from api import app
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
    Function enables user to add an answer to a question on the platform by
    first checking for an empty string in which case it returns an error
    message and then checks if the questionId corresponds to any
    entry in the list of questions, enables the user to enter an
    answer to that specific question and appends the answer to a list of
    answers.

    :param questionId:
    Parameter holds an integer value of the question id to be answered. If
    the value is not an integer value, a TypeError is raised by the method
    which asks the user to enter a number.
    """
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
            'message': 'Question id must be a number!'
        }), 400


@mod.route('/questions/<int:questionId>', methods=['GET'])
def get_one_question(questionId):
    """
    Function enables a user to fetch a single question from the platform
    using the questionId by checking if that id corresponds to any
    question in the list in which case it returns a success message
    with the question that has been fetched. In a case where the question
    id does not match, an error message is returned stating that the
    question does not exist.

    :param questionId:
    Parameter holds an integer value of the question id which is the id
    of the question that the user user to fetch.
    """
    try:
        if questionId > len(questions) or questionId <= 0:
            return jsonify({
                'message': 'Question does not exist.'
            }), 400
        question = questions[questionId - 1]
        return jsonify({
            'Question': question.__dict__,
            'message': 'Question fetched successfully'
        }), 200
    except TypeError:
        return jsonify({
            'message': 'Question id must be a number!'
        }), 400
