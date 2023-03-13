import React, { Component } from 'react';
import './Instructions.css';
import Trie_example from './Trie_example.svg.png';
import knightmoves from './knightmoves.png';
import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';
export default class Code extends Component {

  render() {
    return(
    <React.Fragment>
    <Container>
    <h2>It's all about the source code, baby!</h2>
    <p>If you would like to grab a copy of this react frontend with everything neatly packed up; then you should check out this <a href="https://github.com/mistressAlisi/KnightsTour/" target="_blank">CS Trinkets @ Github repository</a>.
     </p>
     <br/>

     <h4>Zip* Rotate 90 degrees right:</h4>
      <Card>
      <Card.Body>
          <code>
          matrix = list(zip(*reversed(matrix)))
          </code>
      </Card.Body>
      </Card>
     <br/>
     <h4>Zip* Rotate 90 degrees left:</h4>
      <Card>
      <Card.Body>
          <code>
          matrix = list(reversed(list(zip(*matrix))))
          </code>
      </Card.Body>
      </Card>
     <br/>
      <h4>Zip* Vertical operator:</h4>
      <Card>
      <Card.Body>
          <code>
          matrix = list(zip(*(matrix)))
          </code>
      </Card.Body>
      </Card>
     <br/>

      <h4>NumPy Rotate by 90 degrees right/clockwise:</h4>
      <Card>
      <Card.Body>
          <code>
          matrix = np.rot90(matrix,k=1,axes=(1,0)).tolist()
          </code>
      </Card.Body>
      </Card>
     <br/>
      <h4>NumPy Rotate by 90 degrees left/anti-clockwise:</h4>
      <Card>
      <Card.Body>
          <code>
            matrix = np.rot90(matrix,k=1,axes=(0,1)).tolist()
          </code>
      </Card.Body>
      </Card>
     <br/>
      <h4>NumPy Roll by N  places left/anti-clockwise:</h4>
      <Card>
      <Card.Body>
          <code>
           matrix = np.roll(matrix,N*-1).tolist()
          </code>
      </Card.Body>
      </Card>
     <br/>
      <h4>NumPy Roll by N places right/clockwise:</h4>
      <Card>
      <Card.Body>
          <code>
           matrix = np.roll(matrix,N).tolist()
          </code>
      </Card.Body>
      </Card>
     <br/>
    <h4>Numpy 180 degree rotate:</h4>
      <Card>
      <Card.Body>
          <code>
            matrix = np.rot90(np.rot90(matrix,k=1,axes=(1,0)),k=1,axes=(1,0)).tolist()
          </code>
      </Card.Body>
      </Card>
     <br/>

    </Container>
    </React.Fragment>
    )
  }

}
