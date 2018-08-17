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
        "id": questionId,
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
    questionId = int(questionId)
    try:
        if len(questions) < 0:
            return jsonify({
                'message': 'You have no questions yet.'
            }), 400
        question = questions[questionId - 1]
        return jsonify({
            'Question': question.__dict__,
            'Message': 'Question fetched successfully!'
        }), 200
    except IndexError:
        return jsonify({
            'message': 'Question does not exist.'
        }), 400


@mod.route('/questions', methods=['GET'])
def get_all_questions():
    """
    Function enables a user to fetch all questions on the platform by checking
    if the length of the questions list is not zero, in which case it returns
    an error message telling the user there are no questions in the list yet
    else, it returns all the questions in the list of questions on the
    platform.
    """
    if len(questions) == 0:
        return jsonify({
            'message': 'Sorry there are no questions yet!'
        }), 400
    return jsonify({
        'Questions': [question.__dict__ for question in questions],
        'message': 'Questions fetched successfully!'
    }), 200
