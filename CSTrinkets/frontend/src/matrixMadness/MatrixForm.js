// Import React and bootstrap:
import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';
import ThemeProvider from 'react-bootstrap/ThemeProvider';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import InputGroup from 'react-bootstrap/InputGroup';
// Define our Matrix input consts
const matrixY = ['A','B','C','D','E','F','G','H',"J","I","K","L"]
const matrixX = ['1','2','3','4','5','6','7','8',"9","10","11","12"]



// The actual Class is here:
export default class MatrixForm extends Component {
  // We remember our state:
  state = {
   size: 6
  }
  handleSlider = (evt,v) => {
      this.setState({size:(evt.target.value*1)});
  }


  render() {
    return(
    <React.Fragment>

        <InputGroup.Text>Matrix Size :</InputGroup.Text>
        <Form.Range min="2" max="12" default="6" onChange={this.handleSlider} />
     <hr/>
     {[...Array(this.state.size)].map((elementInArray, index) => (
        <Row className="mb-3">

        {[...Array(this.state.size)].map((elementInArray, index2) => (
          <Col>
          <Form.Control size="sm" type="text" id={"m_"+index+"."+index2} name={"m_"+index+"."+index2} placeholder={index+index2} value={matrixY[index]+matrixX[index2]}/>
          </Col>

        )
        )}
        </Row>
    )
    )}

  <Form.Control type="hidden" name="dim" value={this.state.size}/>
  </React.Fragment>

    )
  }

}


