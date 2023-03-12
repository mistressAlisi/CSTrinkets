
import 'bootstrap/dist/css/bootstrap.min.css';
import logo from './logo.svg';
import './App.css';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import Instructions from './knightsTour/Instructions.js'
import TryMe from './knightsTour/TryMe.js'
import Code from './knightsTour/Code.js'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
        <a href="https://github.com/mistressAlisi/KnightsTour/" target="_blank">The Knight's tour</a> in React+Bootstrap.
        </p>
      </header>

    <Tabs
      defaultActiveKey="home"
      id="fill-tab-example"
      className="mb-3"
      fill>
      <Tab eventKey="home" title="Welcome to the Knights Tour!">
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

export default App;
