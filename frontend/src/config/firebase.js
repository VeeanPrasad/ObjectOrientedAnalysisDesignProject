import firebase from "firebase/app";
import "firebase/database";

//import { FirebaseConfig } from "../config/keys";
const FirebaseConfig = {
  apiKey: "AIzaSyC3ZvpYCjRW3maoL3dbscjNdR9BNI4FGxE",
  authDomain: "sem-project-7906f.firebaseapp.com",
  databaseURL: "https://sem-project-7906f.firebaseio.com",
  projectId: "sem-project-7906f",
  storageBucket: "sem-project-7906f.appspot.com",
  messagingSenderId: "1010082860222",
  appId: "1:1010082860222:web:786ae276c9eed59e7e62ef",
  measurementId: "G-DVHCWBB0X0"
};
firebase.initializeApp(FirebaseConfig);

export const databaseRef = firebase.database().ref();

export const gamesRef = databaseRef.child("games");
//export const channelRef = databaseRef.child(`games/${}`);
// export const imagesRef = databaseRef.child("images");

export const newFirebaseId = databaseRef.push().key;
