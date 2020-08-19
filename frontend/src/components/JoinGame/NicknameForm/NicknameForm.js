import React, { Component } from "react";
import "./NicknameForm.scss";
import Button from "../../sharedUI/Button/Button";
import Input from "../../sharedUI/Input/Input";
import { Route } from "react-router-dom";

class NicknameForm extends Component {
  constructor() {
    super();
    this.state = {
      nickname: ""
    };
    this._handleNicknameInput = this._handleNicknameInput.bind(this);
  }

  _handleNicknameInput(event) {
    this.setState({ nickname: event.target.value });
  }

  render() {
    return (
      <div class="limiter">
        <div class="container-login100">
          <div className="nickname">
          <form className="nickname__form">
            <span class="login100-form-title">
              Enter Your Nickname
            </span>
            <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
              <input class="input100" type="text" onChange={this._handleNicknameInput} value={this.state.nickname} />
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-envelope" aria-hidden="true"></i>
              </span>
            </div>
            <Route
              render={({ history }) => (
            <div class="container-login100-form-btn">
              <button class="login100-form-btn" onClick={event => {
                            event.preventDefault();
                            this.props.submitNickname(this.state.nickname);
                            history.push({
                              pathname: "/waiting-room",
                              state: {
                                gamePin: this.props.gamePin,
                                nickname: {
                                  nickname: this.state.nickname,
                                  points: 0,
                                  answer: "",
                                  entered: false,
                                  score: 0,
                                  correct_answers: 0,
                                  streak: 0,
                                  last_correct: false,
                                },
                                isAdmin: false
                              }
                            });
                          }}

                        > Enter </button>
            </div>
          )}
          />
          </form>
          </div>
          </div>
          </div>
    );
  }
}

export default NicknameForm;
