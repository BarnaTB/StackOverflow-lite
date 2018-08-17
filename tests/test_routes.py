import unittest
from api import app
import json


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

        self.assertEqual(reply["message"], "Sorry, you didn\'t enter any question!")

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
            content_type='applcation/json',
            data=json.dumps(question)
        )

        self.assertEqual(response.status_code, 200)

    def test_get_all_questions(self):
        question = dict(
            details='this is my question'
        )

        self.tester.post(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )

        response = self.tester.get(
            'api/v1/questions',
            content_type='application/json',
            data=json.dumps(question)
        )

        self.assertEqual(response.status_code, 200)
