## OOAD Project 6 - Final Submission

### Title: KALE, a game-based education app for quizzes

### Team members: Janani Selvan, Keyur Shirgaonkar, Veena Prasad


#### Instructions to run Frontend:

cd ooad-kale-repo/frontend

npm install

npm start

#### Instructions to run Backend:

cd ooad-kale-repo/Backend

pip3 install -r requirements.txt

python3 backend/app.py runserver

#### Patterns

Singelton - Pin Generator which generates unique pin for the quiz.

Fascade - Seed script that populates the questions, answers, quizzes in the database.

Chain of responsibility - used by game services to parse the params,create game instnac, update redis.

MVC - The structure of the code was based on MVC pattern for better development and maintainance.

Observer - Firebase realtime database implementation.

Decorator -  Adding Corse headers to the responses.





