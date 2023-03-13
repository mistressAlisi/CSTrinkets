import React, { Component } from 'react';
import './Instructions.css';
import Trie_example from './Trie_example.svg.png';
import knightmoves from './knightmoves.png';
import Container from 'react-bootstrap/Container';
export default class Code extends Component {

  render() {
    return(
    <React.Fragment>
    <Container>
    <h2>The knights' tour in code!</h2>
     <p>You can find the original Knights Tour code on my <a href="https://github.com/mistressAlisi/KnightsTour/" target="_blank">KnightsTour @ Github</a>.
     </p>
     <p>If you would like to grab a copy of the react frontend with everything neatly packed up; then you should check out this <a href="https://github.com/mistressAlisi/KnightsTour/" target="_blank">CS Trinkets @ Github repository</a>.
     </p>
     </Container>
    </React.Fragment>
    )
  }

}
