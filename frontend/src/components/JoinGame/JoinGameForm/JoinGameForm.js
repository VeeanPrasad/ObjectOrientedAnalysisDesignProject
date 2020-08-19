import React, { Component } from 'react';
import './JoinGameForm.scss';
//import './main.css';
//import './util.css';
import { Link } from "react-router-dom";
import Button from '../../sharedUI/Button/Button'
import Input from '../../sharedUI/Input/Input'

class JoinGameForm extends Component {
    constructor() {
        super();
        this.state = {
            pin: ""
        }
        this._handlePinInput = this._handlePinInput.bind(this)
    }

    _handlePinInput(event) {
       this.setState({pin: event.target.value});
    }

    render() {
        return (

          <div class="limiter">
            <div class="container-login100">
              <div className="joingame">
              <form className="joingame__form">
                <span class="login100-form-title">
                  Enter Quiz ID
                </span>
                <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
                  <input class="input100" type="text" onChange={this._handlePinInput} value={this.state.pin} name="email" placeholder="Quiz Pin"/>
                  <span class="focus-input100"></span>
                  <span class="symbol-input100">
                    <i class="fa fa-envelope" aria-hidden="true"></i>
                  </span>
                </div>

                <div class="container-login100-form-btn">
                  <button class="login100-form-btn" onClick={event => {
                    event.preventDefault();
                    this.props.click(this.state.pin);
                  }} type="button" > Join Game </button>
                  <Link className = "small" to="/login">Login To Create Quiz</Link>
                </div>
              </form>
              </div>
              </div>
              </div>

        )
    }
}

export default JoinGameForm;
