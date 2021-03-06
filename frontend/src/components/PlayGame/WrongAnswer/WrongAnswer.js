import React, { Component } from 'react';
import "./WrongAnswer.scss"
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTimesCircle } from '@fortawesome/free-solid-svg-icons'
import { gamesRef } from "../../../config/firebase"

library.add(faTimesCircle)


class WrongAnswer extends Component {

    render() {
        // const gameRef = gamesRef.child(this.props.gamesPin);
        // gameRef.on('value', snapshot => {
        //     if (snapshot.val().getOffResults === 0) {
        //         this.props.resetTimer(0)
        //         gameRef.child('getOffResult').set(1)
        //         this.props.resetAnswer( false )
        //     }
        // })
        // this.props.resetAnswer( false )
        return (
            <div className="wronganswer">

                <div className="wronganswer__content">
                    <p className="wronganswer__heading">Wrong!</p>
                    <FontAwesomeIcon className="wronganswer__icon" icon="times-circle" />
                    <p className="wronganswer__body">Your Score Is: { this.props.score }</p>
                </div>
            </div>
        )
    }
}

export default WrongAnswer;