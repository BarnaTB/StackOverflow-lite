users = []
questions = []
answers = []


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Question:
    def __init__(self, question_id, details):
        self.question_id = question_id
        self.details = details


class Answer:
    def __init__(self, answer_id, details):
        self.answer_id = answer_id
        self.details = details
