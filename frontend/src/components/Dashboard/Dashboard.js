import React, { Component } from "react";
import { Link } from "react-router-dom";
import "./Dashboard.scss";
import axios from "axios";
import Card from "./Card/Card";
import { Redirect } from "react-router-dom";

import { gamesRef } from "../../config/firebase";

const QUIZ_URL = "http://localhost:5000/quizzes/list";

const SERVER_URL_PUT = "http://localhost:5000/new_game.json";
const SERVER_URL_GET = "http://localhost:5000/new_game.json";

class Dashboard extends Component {
  constructor() {
    super();
    this.state = {
      quizzes: [],
      redirect: false
    };
    this.componentDidMount = this.componentDidMount.bind(this);
    this._handleCardClick = this._handleCardClick.bind(this);
  }

  componentDidMount() {
    const config = {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("jwt")
      }
    };

    axios.get(QUIZ_URL, config).then(quizzes => {
      this.setState({
        quizzes: quizzes.data
      });
    });
  }

  _handleCardClick(questions) {
    console.log("handle card click");
    //axios.post(SERVER_URL_PUT, { new_game: true, quiz_id: 8 }).then(results => {
    //axios.get(SERVER_URL_GET).then(result => {
    // gamesRef.child().set(
    //   {
    //     players: [""],
    //     questions,
    //     next_question: 0,
    //     currentQuestion: questions[0].content,
    //     currentAnswers: questions[0].answers.map(answer => answer.answer)
    //   },
    //   error => {
    //     if (error) {
    //       console.error(error);
    //     } else {
    //       this.setState({ redirect: true, gameId: result.data.id });
    //     }
    //   }
    // );
    //  });
    //});
  }

  renderCards() {
    return this.state.quizzes.map(quiz => {
      return (
        <Link
          to={{
            pathname: "/waiting-room",
            state: {
              questions: quiz.questions,
              isAdmin: true
            }
          }}
          key={quiz.id}
        >
          <Card
            key={quiz.id}
            category={quiz.category}
            difficulty={quiz.difficulty}
            questions={quiz.questions}
          />
        </Link>
      );
    });
  }

  render() {
    if (localStorage.getItem("jwt")) {
      return (
        <div className="displayQuizzes">
          <div className="header">
            <h1>Choose a game to play</h1>
          </div>

          {<div className="displayCards">{this.renderCards()}</div>}
        </div>
      );
    } else {
      return <Redirect to="/" />;
    }
  }
}

export default Dashboard;
