from api.models import *


def get_question(questionId):
    for question in questions:
        if question.questionId == questionId:
            return question
