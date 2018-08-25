import unittest
from api import app
import json
from api.models import *


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_add_question(self):
        question = dict(
            details='details'
        )
        response = self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )
        reply = json.loads(response.data.decode())

        self.assertEqual(reply["message"], "Question added successfully!")

    def test_add_question_empty_string(self):
        question = dict(
            details=''
        )
        response = self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )
        reply = json.loads(response.data.decode())

        self.assertEqual(reply["message"], "Sorry, you didn't enter any question!")

    def test_add_question_user_enters_a_space(self):
        question = dict(
            details=' '
        )
        response = self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )
        reply = json.loads(response.data.decode())

        self.assertEqual(reply["message"], "Sorry, you didn't enter any question!")

    def test_get_one_question(self):
        question = dict(
            details='this is my question'
        )

        self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )
        response = self.tester.get(
            'api/v1/questions/1',
        )

        self.assertEqual(response.status_code, 200)

    def test_get_one_question_if_there_are_no_questions_yet(self):
        response = self.tester.get(
            'api/v1/questions/1'
        )

        if len(questions) < 0:
            self.assertEqual(
                response['message'], 'You have no questions yet.'
                )

    def test_get_one_question_out_of_index(self):
        question = dict(
            details='my question'
        )

        self.tester.post(
            'api/v1/questions',
            content_type='applcation/json',
            data=json.dumps(question)
        )

        response = self.tester.get(
            'api/v1/questions/2'
        )

        if len(questions) == 1:
            # self.assertEqual(
            #     response['message'], 'Question does not exist.'
            #     )
            self.assertRaises(IndexError, response)

    def test_get_all_questions(self):
        question = dict(
            details='my question'
        )

        self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )

        response = self.tester.get(
            'api/v1/questions'
        )

        self.assertEqual(
            response.status_code, 200
            )

    def test_get_all_questions_from_empty_list(self):
        response = self.tester.get(
            'api/v1/questions/1'
        )

        if len(questions) < 0:
            self.assertEqual(
                response['message'], 'You have no questions yet.'
                )

    def test_delete_question(self):
        question = dict(
            details='my question'
        )

        self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )

        response = self.tester.delete(
            'api/v1/questions/1'
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_question_which_does_not_exist(self):
        question = dict(
            details='my question'
        )

        self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )

        response = self.tester.delete(
            'api/v1/questions/3'
        )

        if len(questions) == 1:
            self.assertEqual(response.status_code, 404)

    def test_delete_questions_from_empty_list(self):
        response = self.tester.get(
            'api/v1/questions/1'
        )

        if len(questions) < 0:
            self.assertEqual(
                response['message'], 'There are no questions to delete!'
                )


class TestAnswer(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_add_answer_without_question(self):
        answer = dict(
            details="my answer"
        )

        response = self.tester.post(
            'api/v1/questions/1/answers',
            content_type='application/json',
            data=json.dumps(answer)
        )

        if len(questions) == 0:
            self.assertEqual(
                response.status_code, 404
                )
            self.assertRaises(IndexError, response)

    def test_add_answer_without_details(self):
        question = dict(
            details="my question"
        )

        answer = dict(
            details=""
        )

        self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )

        response = self.tester.post(
            'api/v1/questions/1/answers',
            content_type='application/json',
            data=json.dumps(answer)
        )

        self.assertEqual(
            response.status_code, 400
            )

    def test_add_answer_with_both_answer_and_question_details(self):
        question = dict(
            details="my question"
        )

        answer = dict(
            details="my answer"
        )

        self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )

        response = self.tester.post(
            'api/v1/questions/1/answers',
            content_type='application/json',
            data=json.dumps(answer)
        )

        self.assertEqual(
            response.status_code, 201
            )

    def test_add_answer_to_question_which_does_not_exist(self):
        question = dict(
            details="my question"
        )

        answer = dict(
            details="my answer"
        )

        self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )

        response = self.tester.post(
            'api/v1/questions/2/answers',
            content_type='application/json',
            data=json.dumps(answer)
        )

        if len(questions) == 1:
            self.assertEqual(
                response.status_code, 404
                )


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_registration_empty_username(self):
        user = dict(
            username="",
            email="barna@gmail.com",
            password="123456"
        )

        response = self.tester.post(
                'api/v1/signup',
                content_type='application/json',
                data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(
            reply["message"], "Sorry, you did not enter your username!"
            )

    def test_registration_spaces_entry(self):
        user = dict(
            username=" ",
            email="barna@gmail.com",
            password="123456"
        )

        response = self.tester.post(
                'api/v1/signup',
                content_type='application/json',
                data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(
            reply["message"], "Sorry, you did not enter your username!"
            )

    def test_registration_email_empty(self):
        user = dict(
            username="Barna",
            email="",
            password="123456"
        )

        response = self.tester.post(
                'api/v1/signup',
                content_type='application/json',
                data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(
            reply["message"], "Sorry, you did not enter your email!"
            )

    def test_registration_email_space_entry(self):
        user = dict(
            username="Barna",
            email=" ",
            password="123456"
        )

        response = self.tester.post(
                'api/v1/signup',
                content_type='application/json',
                data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply["message"], "Sorry, you did not enter your email!")

    def test_registration_email_vague_data(self):
        user = dict(
            username="Barna",
            email="barna@..Com",
            password="123456"
        )

        response = self.tester.post(
                'api/v1/signup',
                content_type='application/json',
                data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply["message"], "Invalid email address!")

    def test_registration_password_empty(self):
        user = dict(
            username="Barna",
            email="barna@gmail.Com",
            password=""
        )

        response = self.tester.post(
                'api/v1/signup',
                content_type='application/json',
                data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply["message"], "Sorry, you did not enter your password!")

    def registration_password_spaces_entry(self):
        user = dict(
            username="Barna",
            email="barna@gmail.Com",
            password=" "
        )

        response = self.tester.post(
                'api/v1/signup',
                content_type='application/json',
                data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(
            reply["message"], "Sorry, you did not enter your password!"
            )

    def test_password_length_below_6(self):
        user = dict(
            username="Barna",
            email="barna@gmail.com",
            password="12bar"
        )

        response = self.tester.post(
                'api/v1/signup',
                content_type='application/json',
                data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(
            reply["message"], "Passwords should be at least 6 characters long!"
            )

    def test_password_correct(self):
        user = dict(
            username="Barna",
            email="barna@gmail.com",
            password="1234567"
        )

        response = self.tester.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply["message"], "Barna has registered successfully")

    def test_user_login_empty_username(self):
        user = dict(
            username='',
            password='aoixamklx'
        )

        response = self.tester.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'You did not enter your username!')

    def test_user_login_space_username(self):
        user = dict(
            username=' ',
            password='aoixamklx'
        )

        response = self.tester.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'You did not enter your username!')

    def test_user_login_empty_password(self):
        user = dict(
            username='Barna',
            password=''
        )

        response = self.tester.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'You did not enter your password!')

    def test_user_login_space_password(self):
        user = dict(
            username='Barna',
            password=' '
        )

        response = self.tester.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'You did not enter your password!')

    def test_user_login_successfully(self):
        user = dict(
            username='Barna',
            password='asxon[8'
        )

        response = self.tester.post(
            'api/v1/login',
            content_type='application/json',
            data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'Barna is logged in.')


class ModelsTests(unittest.TestCase):
    def test_user_model(self):
        user = User('1', 'Barna', 'barna@gmail.com', '12345')

    def test_question_model(self):
        question = Question('1', 'what is coding?')

    def test_answer_model(self):
        answer = Answer('1', 'code is obulamu')