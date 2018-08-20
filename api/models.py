from passlib.hash import pbkdf2_sha256 as sha256


users = []
questions = []
answers = []


class User:
    def __init__(self, user_id, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def generate_hash(self, password):
        return sha256.hash(self.password)

    @staticmethod
    def verify_hash(self, password):
        return sha256.verify(password, hash)


class Question:
    def __init__(self, questionId, details):
        self.questionId = questionId
        self.details = details


class Answer:
    def __init__(self, questionId, details):
        self.questionId = questionId
        self.details = details
