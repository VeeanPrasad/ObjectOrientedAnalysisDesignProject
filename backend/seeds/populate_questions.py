from backend.models.user import User
from backend.models.quiz import Quiz, Question
from backend.models.answer import Answer
import requests
from flask_sqlalchemy import SQLAlchemy
from manager import create_app


# Fascade pattern: The creation of question, options and edition of questions are 
# encapsulated within the Seed Fascade manager.It forms as a simplified interface 
# for a class library.

seed_app = create_app()
db_obj = SQLAlchemy(seed_app)

class Deletor(object):
    def handle(self):
        User.query.delete()
        Question.query.delete()
        Quiz.query.delete()
        Answer.query.delete()

class QuestionCreator(object):
    def handle(self, content, answer_objs):
        return Question(content=content, answers=answer_objs)

class AnswerCreator(object):
    def handle(self, answers):
        answer_objs = []
        for index, answer in enumerate(answers):
            if index == 3:
                answer_objs.append(Answer(answer=answer, correct=True))
            else:
                answer_objs.append(Answer(answer=answer, correct=False))
        return answer_objs

class QuizCreator(object):
    def __init__(self):
        self.question_creator = QuestionCreator()
        self.answer_creator = AnswerCreator()

    def handle(self, data, difficulty):
        question_array = data["results"]
        question_objs = []

        for question in question_array:
            answers = question["incorrect_answers"]
            answers.append(question["correct_answer"])
            answer_objs = self.answer_creator.handle(answers)
            quest = self.question_creator.handle(question["question"], answer_objs)
            question_objs.append(quest)

        quiz = Quiz({"category": question_array[0]["category"], "difficulty": difficulty})
        quiz.questions = question_objs

        return quiz


class SeedFacadeManager(object):
    difficulties = ['easy', 'medium', 'hard']
    categories_index = range(9,10)

    def __init__(self):
        self.deletor = Deletor()
        self.quiz_creator = QuizCreator()

    def handle(self):
        for category in SeedFacadeManager.categories_index:
            for difficulty in SeedFacadeManager.difficulties:
                url = "https://opentdb.com/api.php?amount=10&category={}&difficulty={}&type=multiple".format(category, difficulty)
                r = requests.get(url=url)
                document = r.json()
                if document["response_code"] == 1: break ## this is the api code for no content, so just break

                quiz_obj = self.quiz_creator.handle(document, difficulty)

                db_obj.session.add(quiz_obj)
                db_obj.session.commit()


seed_facade_manager = SeedFacadeManager()
seed_facade_manager.handle()

