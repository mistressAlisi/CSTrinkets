import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import logo from './logo.svg';
import './MatrixMadness.css';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import Instructions from './matrixMadness/Instructions.js'
import TryMe from './matrixMadness/TryMe.js'
import Code from './matrixMadness/Code.js'
import ListGroup from 'react-bootstrap/ListGroup';
function MatrixMadness() {
  return (
    <div className="KnightsTour">
      <header className="KnightsTour-header">
        <img src={logo} className="KnightsTour-logo" alt="logo" />
        <p>
        Matrix Madness!
        </p>
      </header>

    <Tabs
      defaultActiveKey="home"
      id="fill-tab-example"
      className="mb-3"
      fill>
      <Tab eventKey="home" title="Its a Mad Matrix World!">
  <Instructions />
      </Tab>
      <Tab eventKey="tryme" title="Try it out!">
  <TryMe/>
      </Tab>
      <Tab eventKey="code" title="The Code">
      <Code />
      </Tab>

    </Tabs>
    </div>
  );
}

export default MatrixMadness;
