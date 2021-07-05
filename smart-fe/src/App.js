import React, { Component, Fragment } from "react";
import './App.css';
import NewTshirtForm from './components/NewTshirtForm';
import NewShoesForm from './components/NewShoesForm';
import Header from "./components/Header";
import Navbar from "./components/Navbar";
import './index.css';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useRouteMatch
} from "react-router-dom";


function App() {
  return (
    
    <div>
      <Fragment>
          <h2 id="shop_title">Welecome To Pro Shop!</h2>
          <Navbar/>
          <img id="image1" src="https://i.pinimg.com/originals/95/39/18/95391814eb00381fd10223ebffdea238.jpg"/>
      </Fragment>
    </div>


    //<div className="row"><NewTshirtForm/></div>
    // <div className="row"><NewShoesForm/></div>
  );
}

export default App;
