import psycopg2
from pprint import pprint


class DbConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='stackoverflow' password='##password' host='localhost' port='5432'"
            )
            self.cursor = self.connection.cursor()
            self.connection.autocommit = True
        except:
            pprint("Failed to connect to database!")

    def create_user_table(self):
        create_user_table_command = "CREATE TABLE user(id SERIAL PRIMARY KEY, userId INTEGER NOT NULL, username VARCAHR(100), email VARCHAR(100) NOT NULL, password VARCHAR(255) NOT NULL);"
        self.cursor.execute(create_user_table_command)

    def fetch_user_by_name(self, username):
        fetch_username_command = "SELECT * FROM user WHERE username = {};".format(username)
        self.cursor.execute(fetch_username_command)
        user = self.cursor.fetchall()

        return user

    def insert_user(self, userId, username, email, password):
        insert_user_command = "INSERT INTO user(userId, username, email, password) VALUES({}, {}, {}, {});".format(userId, username, email, password)
        self.cursor.execute(insert_user_command)

    def create_question(self):
        create_question_command = "CREATE TABLE question(userId INTEGER NOT NULL, questionId INTEGER NOT NULL, details VARCHAR(255) NOT NULL);"
        self.cursor.execute(create_question_command)

    def insert_question(self, userId, questionId, details):
        insert_question_command = "INSERT INTO question(userId, questionId, details) VALUES({}, {}, {});".format(userId, questionId, details)
        self.cursor.execute(insert_question_command)

    def fetch_questions(self, userId):
        fetch_questions_command = "SELECT * FROM question WHERE userId={};".format(userId)
        self.cursor.execute(fetch_questions_command)
        qns = self.cursor.fetchall()

        return qns

    def fetch_one_question(self, userId, questionId):
        fetch_one_question_command = "SELECT userId, questionId, question.details, answer.details FROM question, answer WHERE userId={} AND answer.questionId={};".format(userId, questionId)
        self.cursor.execute(fetch_one_question_command)
        qn = self.cursor.fetchall()

        return qn

    def delete_question(self, userId, questionId):
        delete_question_command = "DELETE FROM question WHERE userId={} AND questionId={};".format(userId, questionId)
        self.cursor.execute(delete_question_command)

    def create_answer_table(self):
        create_answer_table_command = "CREATE TABLE answer(id INTEGER SERIAL PRIMARY KEY, userId INTEGER NOT NULL, questionId INTEGER NOT NULL, details VARCHAR(255) NOT NULL, preference BOOLEAN);"
        self.cursor.execute(create_answer_table_command)

    def insert_answer(self, userId, questionId, details):
        insert_answer_command = "INSERT INTO answer(userId, questionId, details) VALUES({}, {}, {});".format(userId, questionId, details)
        self.cursor.execute(insert_answer_command)

    def delete_answer(self, userId, questionId):
        delete_answer_command = "DELETE FROM answer WHERE userId={} AND questionId={};".format(userId, questionId)
        self.cursor.execute(delete_answer_command)

    def prefer_answer(self, userId, questionId):
        prefer_answer_command = "UPDATE answer SET preference='Preferred' WHERE userId={} AND questionId={};".format(userId, questionId)
        self.cursor.execute(prefer_answer_command)
