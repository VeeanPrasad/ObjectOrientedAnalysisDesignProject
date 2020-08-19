import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";
import "./SignUp.scss";
import Input from "../sharedUI/Input/Input";
import Button from "../sharedUI/Button/Button";
import axios from "axios";
import gk from "./kale.png";

const USER_CREATE_URL = "http://localhost:5000/users/create";
const USER_TOKEN_URL = "http://localhost:5000/quizzes/user_token";

export default class SignUp extends Component {
  constructor() {
    super();
    this.state = {
      email: "",
      password: "",
      password_confirmation: "",
      login: false,
      error: false
    };
    this._handleEmailInput = this._handleEmailInput.bind(this);
    this._handlePasswordInput = this._handlePasswordInput.bind(this);
    this._handlePasswordAgainInput = this._handlePasswordAgainInput.bind(this);
    this._handleSignupSubmit = this._handleSignupSubmit.bind(this);
  }

  _handleEmailInput(event) {
    this.setState({ email: event.target.value });
  }

  _handlePasswordInput(event) {
    this.setState({ password: event.target.value });
  }

  _handlePasswordAgainInput(event) {
    this.setState({ password_confirmation: event.target.value });
  }

  _handleSignupSubmit(event) {
    event.preventDefault();
    localStorage.setItem("jwt", undefined);

    const { email, password, password_confirmation } = this.state;

    const request = {
      email: email,
      password: password,
      password_confirmation: password_confirmation
    };

    axios.post(USER_CREATE_URL, request).then(response => {
      console.log("succesfully created the user with ", response);

      axios
        .post(USER_TOKEN_URL, { auth: { email: email, password: password } })
        .then(data => {
          if (data.status === 201) {
            localStorage.setItem("jwt", data.data.jwt);
            this.setState({ login: true });
          }
        })
        .catch(error => {
          this.setState({ error: true });
        });
    });
    //BENS FUNCTION
  }

  render() {
    const { error, login } = this.state;
    if (error === false && login === false) {
      return (
        <div className="login">
    <form className="login__form">
    <div class="limiter">
      <div class="container-login100">
        <div class="wrap-login100">
          <div class="login100-pic js-tilt" data-tilt>
            <img src={gk} alt=""/>
          </div>

          <form class="login100-form validate-form">
            <span class="login100-form-title">
              SignUp
            </span>
            <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
              <input class="input100" type="email"
                    placeholder="Enter Email"
                    value={this.state.email}
                    onChange={this._handleEmailInput}/>
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-envelope" aria-hidden="true"></i>
              </span>
            </div>

            <div class="wrap-input100 validate-input" data-validate = "Password is required">
              <input class="input100" type="password"
                    placeholder="Password"
                    value={this.state.password}
                    onChange={this._handlePasswordInput}/>
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-lock" aria-hidden="true"></i>
              </span>
            </div>

            <div class="wrap-input100 validate-input" data-validate = "Password is required">
              <input class="input100" type="password"
                    placeholder="Password Confirmation"
                    value={this.state.password_confirmation}
                    onChange={this._handlePasswordAgainInput}/>
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-lock" aria-hidden="true"></i>
              </span>
            </div>



            <div class="container-login100-form-btn">
              <button class="login100-form-btn" type="button" text="SignUp" onClick={this._handleSignupSubmit}>
              Sign Up
              </button>
              <Link to="/login" className="small">Already Have An Account? Login</Link>
            </div>
              </form>
              </div>
              </div>
              </div>
            </form>
          </div>

      );
    } else if (login === false && error === true) {
      return (
        <div className="login">
    <form className="login__form">
    <div class="limiter">
      <div class="container-login100">
        <div class="wrap-login100">
          <div class="login100-pic js-tilt" data-tilt>
            <img src={gk} alt=""/>
          </div>

          <form class="login100-form validate-form">
            <span class="login100-form-title">
              SignUp
            </span>
            <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
              <input class="input100" type="email"
                    class="input"
                    placeholder="Enter Email"
                    value={this.state.email}
                    onChange={this._handleEmailInput}/>
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-envelope" aria-hidden="true"></i>
              </span>
            </div>

            <div class="wrap-input100 validate-input" data-validate = "Password is required">
              <input class="input100" type="password"
                    class="input"
                    placeholder="Password"
                    value={this.state.password}
                    onChange={this._handlePasswordInput}/>
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-lock" aria-hidden="true"></i>
              </span>
            </div>

            <div class="wrap-input100 validate-input" data-validate = "Password is required">
              <input class="input100" type="password"
                    class="input"
                    placeholder="Password Confirmation"
                    value={this.state.password_confirmation}
                    onChange={this._handlePasswordAgainInput}/>
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-lock" aria-hidden="true"></i>
              </span>
            </div>



            <div class="container-login100-form-btn">
              <button class="login100-form-btn" type="button" text="SignUp" onClick={this._handleSignupSubmit}>
              Sign Up
              </button>
              <Link to="/login" className="small">Already Have An Account? Login</Link>
            </div>
              </form>
              </div>
              </div>
              </div>
            </form>
          </div>

      );
    }
    return <Redirect to="/dashboard" />;
  }
}
