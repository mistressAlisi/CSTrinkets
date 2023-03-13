import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import logo from './logo.svg';
import './Landing.css';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';

import ListGroup from 'react-bootstrap/ListGroup';
function Landing() {
  return (
    <div className="Landing">
      <header className="Landing-header">
        <img src={logo} className="Landing-logo" alt="logo" />
        <p>
        <a href="https://github.com/mistressAlisi/" target="_blank">Alisi's</a> CS Trinkets and Toys - a full stack demo.
        </p>
        <p>
        Where would you like to start?
        </p>
        &#160;

      <ListGroup >
       <ListGroup.Item action href="#link2" disabled variant="dark">
       In this Demo:
      </ListGroup.Item>
      <ListGroup.Item action href="/KnightsTour" variant="dark">
        The Knights Tour
      </ListGroup.Item>
      <ListGroup.Item action href="/MatrixMadness" variant="dark">
        Matrix Madness!
      </ListGroup.Item>
      <ListGroup.Item action href="#link2" disabled variant="dark">
       External Sites:
      </ListGroup.Item>
      <ListGroup.Item action href="https://github.com/mistressAlisi/" target="_blank" variant="dark">
        Visit my GitHub
      </ListGroup.Item>
      <ListGroup.Item action href="https://delta9.ooo" target="_blank" variant="dark">
        Visit the Delta9 Website
      </ListGroup.Item>
      <ListGroup.Item action href="https://ply.ooo" target="_blank" variant="dark">
        Visit my Photo Gallery
      </ListGroup.Item>

    </ListGroup>
      </header>


    </div>
  );
}

export default Landing;
