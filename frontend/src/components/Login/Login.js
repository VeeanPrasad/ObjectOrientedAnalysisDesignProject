import React, { Component } from 'react';
import { Redirect } from "react-router-dom";
import { Link } from "react-router-dom";
//import './Login.scss'
import './css/main.css';
import './css/util.css';
import Input from '../sharedUI/Input/Input';
import Button from '../sharedUI/Button/Button';
import axios from 'axios';
import gk from "./images/kale.png";


const USER_TOKEN_URL = "http://localhost:5000/quizzes/user_token" // change to heroku

class Login extends Component {
  constructor() {
    super();
    this.state = {
      email: "",
      password: "",
      login: false,
      error: false,
    }
    this._handleEmailInput = this._handleEmailInput.bind(this)
    this._handlePasswordInput = this._handlePasswordInput.bind(this)
    this._handleLoginSubmit = this._handleLoginSubmit.bind(this)
  }

  _handleEmailInput(event) {
    this.setState({ email: event.target.value })
  }

  _handlePasswordInput(event) {
    this.setState({ password: event.target.value })
  }

  _handleLoginSubmit(event) {
    event.preventDefault();
    // this.setState({ email: this.state.login, password: this.state.password })
    const { email, password } = this.state

    const request = { "auth": { "email": email, "password": password } }
    axios.post(USER_TOKEN_URL, request).then((result) => {
      if ( result.status === 201 ){
        localStorage.setItem('jwt', result.data.jwt)
        this.setState({ login: true })
      } }).catch( error => this.setState({ error: true }))
    }

    //setup logic, here for testing

  render() {
    if ( this.state.login === false && this.state.error === false ){
      return (

        //<audio src="a.mp3" id="my_audio" loop="loop" autoplay="autoplay"></audio>
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
              Member Login
            </span>
            <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
              <input class="input100" type="text" name="email" placeholder="Email" value={this.state.email}
                     onChange={this._handleEmailInput}/>
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-envelope" aria-hidden="true"></i>
              </span>
            </div>

            <div class="wrap-input100 validate-input" data-validate = "Password is required">
              <input class="input100" type="password" name="pass" placeholder="Password" value={this.state.password}
                 onChange={this._handlePasswordInput}/>
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-lock" aria-hidden="true"></i>
              </span>
            </div>

            <div class="container-login100-form-btn">
              <button class="login100-form-btn" onClick={this._handleLoginSubmit}>
                Login

              </button>
              <Link to="/signup" className="small">No Account? SignUp</Link>
            </div>
              </form>
              </div>
              </div>
              </div>
            </form>
          </div>
     );
   }
   else if (this.state.login === false && this.state.error === true ) {
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
              Something went wrong
            </span>
            <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
              <input class="input100" type="text" name="email" placeholder="Email" value={this.state.email}
                     onChange={this._handleEmailInput}/>
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-envelope" aria-hidden="true"></i>
              </span>
            </div>

            <div class="wrap-input100 validate-input" data-validate = "Password is required">
              <input class="input100" type="password" name="pass" placeholder="Password" value={this.state.password}
                 onChange={this._handlePasswordInput}/>
              <span class="focus-input100"></span>
              <span class="symbol-input100">
                <i class="fa fa-lock" aria-hidden="true"></i>
              </span>
            </div>

            <div class="container-login100-form-btn">
              <button class="login100-form-btn" onClick={this._handleLoginSubmit}>
                Login

              </button>
              <Link to="/signup" className="small">No Account? SignUp</Link>
            </div>
              </form>
              </div>
              </div>
              </div>
            </form>
          </div>


    else {
      return ( <Redirect to="/dashboard" />   )
    }

}
};

export default Login;
