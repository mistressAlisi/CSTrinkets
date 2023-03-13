// Import React and bootstrap:

import React, { Component ,useState, useReducer} from 'react';


import Container from 'react-bootstrap/Container';
import ThemeProvider from 'react-bootstrap/ThemeProvider';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
// Also we need axios:
import axios from 'axios';

// Import our stuff:
import MatrixForm from './MatrixForm.js';



// The actual Class is here:
export default class Tryme extends Component {
  // The state of the application will be updated via AXIOS:
  state = {
    longString: '',
    matrix: '',
    debug: ''
  }
   constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);

  }
  handleChange = (evt) => {
    // evt is a change event
    this.setState({
      longString: evt.string,
      matrix: evt.matrix,
      debug: evt.debug
    });
  }
   handleSubmit(event) {
   event.preventDefault();
  var data = new FormData(event.target);

  axios.post("/api/knightsTour/run/",data).then((response) => {
    console.log(response.data.payload.string);
    this.setState({
            string: response.data.payload.string,
            matrix: response.data.payload.matrix,
            debug: response.data.payload.debug
     });

  }).catch(err => {

    console.log(err);
    alert("Error: "+err)
  })
   }




  render() {
    return(
    <React.Fragment>
    <Container>
          <ThemeProvider
  breakpoints={['xxxl', 'xxl', 'xl', 'lg', 'md', 'sm', 'xs', 'xxs']}
  minBreakpoint="xxs"
>
    <form onSubmit={this.handleSubmit}>
    <div class="card-body">
    <h2>Trying out the Tour</h2>
    <p><em>
    Ready to try out the tour? Great! All you need is a text file (or a URL for a text file/html) and a matrix (we provide a default one below) for the chessboard. This page will execute the code on our <a href="https://www.djangoproject.com/" target="_blank">Django</a> backend and render the output for you.
    </em>
    </p>
  <Container>
      <Row>
        <Col sm={8}>
        <Card>
      <Card.Header> <h3>Input Parameters:</h3></Card.Header>
      <Card.Body>
        <Card.Title>Chess Matrix:</Card.Title>
        <Card.Text>
        This is the matrix used for the Chess Board - the ability to change it in the UI is coming soon:
        <br/>
        <MatrixForm />
        <hr/>
        <Card.Title>Text Source:</Card.Title>
         Specify a URL to strip for text, or provide a string of text in the textarea below (the URL takes precedence):
        <br/>
        <br/>
      <Row>
       <InputGroup>
        <InputGroup.Text>Source URL:</InputGroup.Text>
         <Form.Control size="sm" type="text" id="sourceURL" name="url" placeholder="http://..." />
      </InputGroup>
      </Row>

      <br/>
      <Row>
       <InputGroup>
        <InputGroup.Text>Input Text:</InputGroup.Text>
        <Form.Control as="textarea" aria-label="Input Text" name="inputtext"/>
      </InputGroup>
      </Row>
        </Card.Text>

        <Button variant="primary" type="submit">Execute!</Button>
      </Card.Body>
    </Card>
        </Col>
        <Col sm={4}>
        <Card>
        <Card.Header> <h3>Output/Results:</h3></Card.Header>
        <Card.Body>
          <Card.Title>The results are:</Card.Title>
        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
        <Form.Label><strong>Longest Possible String:</strong></Form.Label>
        <Form.Control type="text" placeholder="The longest possible string will appear here!" value={this.state.string} readOnly />
        </Form.Group>

        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
        <Form.Label><strong>Matrix Position:</strong></Form.Label>
        <Form.Control type="text" placeholder="X,Y will appear here!" value={this.state.matrix} readOnly />
        </Form.Group>

        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
        <Form.Label><strong>Timing/Performance Analysis:</strong></Form.Label>
        <Form.Control as="textarea" placeholder="Execute first!" rows="18" value={this.state.debug} readOnly />
        </Form.Group>
        </Card.Body>
        </Card>
        </Col>
      </Row>
    </Container>
  </div>
  </form>
  </ThemeProvider>
  </Container>
  </React.Fragment>

    )
  }

}



