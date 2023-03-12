// Import React and bootstrap:
import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';
import ThemeProvider from 'react-bootstrap/ThemeProvider';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
// Define our Matrix input consts
const matrixY = ['A','B','C','D','E','F','G','H']
const matrixX = ['1','2','3','4','5','6','7','8']

// Matrix Values:
const defMatrix = {
    "A1":"E","A2":"X","A3":"T","A4":"R","A5":"A","A6":"H","A7":"O","A8":"P",
    "B1":"N","B2":"E","B3":"T","B4":"W","B5":"O","B6":"R","B7":"K","B8":"S",
    "C1":"Q","C2":"I","C3":"H","C4":"A","C5":"C","C6":"I","C7":"Q","C8":"T",
    "D1":"L","D2":"F","D3":"U","D4":"N","D5":"U","D6":"R","D7":"X","D8":"B",
    "E1":"B","E2":"W","E3":"D","E4":"I","E5":"L","E6":"A","E7":"T","E8":"V",
    "F1":"O","F2":"S","F3":"S","F4":"Y","F5":"N","F6":"A","F7":"C","F8":"K",
    "G1":"Q","G2":"W","G3":"O","G4":"P","G5":"M","G6":"T","G7":"C","G8":"P",
    "H1":"K","H2":"I","H3":"P","H4":"A","H5":"C","H6":"K","H7":"E","H8":"T"
}

// The actual Class is here:
export default class MatrixForm extends Component {
     render() {
    return(
    <React.Fragment>

     {matrixY.map(mY => (
        <Row className="mb-3">

            {matrixX.map(mX => (
                <Col>
                <Form.Control size="sm" type="text" id={"m_"+mY+"."+mX} name={"m_"+mY+"."+mX} placeholder={mY+mX} value={defMatrix[mY+mX]}/>
                </Col>
            ))}

        </Row>
      ))}

  </React.Fragment>

    )
  }

}


