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
import Table from 'react-bootstrap/Table';
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
    debug: '',
    dim: 0
  }
   constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);

  }
  handleChange = (evt) => {
    // evt is a change event
    this.setState({
      outputString: evt.string,
      outputMatrix: evt.matrix,
      runTime: evt.runtime,
      dim: evt.dim
    });
  }
   handleSubmit(event) {
   event.preventDefault();
  var data = new FormData(event.target);

  axios.post("/api/matrixMadness/run/",data).then((response) => {
    console.log(response.data.payload.string);
    this.setState({
            outputString: response.data.payload.string,
            outputMatrix: response.data.payload.matrix,
            runTime: response.data.payload.runtime,
            dim: response.data.payload.dim
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
    <h2>Its Matrix wrangling time.</h2>
    <p><em>
    First; you can select the size of Matrix you want to play with using the slider. (default is 6x6) - Afterwards, select the algorithm to execute on the Matrix below.  This page will execute the code on our <a href="https://www.djangoproject.com/" target="_blank">Django</a> backend and render the transformed matrix on the right half of the page.
    </em>
    </p>
  <Container>
      <Row>
        <Col sm={8}>
        <Card>
      <Card.Header> <h3>Input Parameters:</h3></Card.Header>
      <Card.Body>
        <Card.Title>Create a Matrix:</Card.Title>
        <Card.Text>
        Use the slider below to generate a NxN matrix to have some fun with:
        <br/>
        <MatrixForm />
        <hr/>
        <Card.Title>Operation Selection:</Card.Title>
         Select which Operation to Perform on your beautiful new matrix:
        <br/>
        <br/>
      <Row>
       <InputGroup>
        <InputGroup.Text>Operation:</InputGroup.Text>
          <Form.Select aria-label="Select Operation" name="oper" id="oper">
              <option value="r90l">Zip* Rotate 90 degrees right</option>
              <option value="l90l">Zip* Rotate 90 degrees left</option>
              <option value="zvo">Zip* Vertical Operator</option>
              <option value="n90r">NumPy Rotate 90 degrees right</option>
              <option value="n180">NumPy Rotate 180 Degrees</option>
              <option value="nrnl">NumPy Roll Array by N places left</option>
              <option value="nrrl">NumPy Roll Array by N places right</option>
              <option value="nr2l">NumPy Roll Array by 2N places left</option>
              <option value="nr2r">NumPy Roll Array by 2N places right</option>

        </Form.Select>
      </InputGroup>
      </Row>
      <br/>
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
        <Form.Label><strong>Matrix in String Form:</strong></Form.Label>
        <Form.Control type="text" placeholder="The flattened Matrix will appear here!" value={this.state.outputString} readOnly />
        </Form.Group>

        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
        <Form.Label><strong>Computation Time:</strong></Form.Label>
        <Form.Control type="text" placeholder="Runtime will appear here!" value={this.state.runTime} readOnly />
        </Form.Group>

        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
        <Form.Label><strong>Matrix Output:</strong></Form.Label>
        <div>
          <Table striped bordered hover>
          {[...Array(this.state.dim)].map((elementInArray, index) => (
              <tr>
              {[...Array(this.state.dim)].map((elementInArray, index2) => (
                 <td>{this.state.outputMatrix[index][index2]}</td>
                )
              )}
              </tr>
            )
          )}
          </Table>

        </div>
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



