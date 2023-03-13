import React, { Component } from 'react';
import './Instructions.css';
import MatrixLabelled from './MatrixLabelled.svg.png';
import knightmoves from './knightmoves.png';
import Container from 'react-bootstrap/Container';

export default class Instructions extends Component {

  render() {
    return(
    <React.Fragment>
    <Container>
    <div class="card-body">
    <h2>Matrices are everywhere in computer science.</h2>
    <p><em>
    And they can be hard, and confusing. I find that a lot of prospective employers gauge your ability as a software engineer (very) heavily on your ability to wrangle Matrices. They are a great proxy for how you think and approach software problems; but they're still hard!
    </em>
    </p>
    <p>
    In this page; I've collected a few real fun tips and tricks, stuff I have written for interviews and the plethora of platforms used to gauge you as an engineer in a few minutes! (Leetcode, HackerRank, CodeSignal, CodePad, they just keep on coming! But they all ask about <em>matrix manipulation.</em>)
    </p>
    <h3>This is a collection of Matrix-wrangling Algorithms that run on Python on the backend.</h3>
    <img src={MatrixLabelled} className="trie-example" alt="MatrixLabelled" />



    <p>
    &#160;
   The code is written with readability and performance in mind:  In order to keep the algorithms fast, efficient and, above all, readable; the solutions are implemented in the most reasonably efficient and pythonic manner of doing things. NumPy is a fantastic, underappreciated library that provides awesome Matrix Math. We also make liberal use of operators like zip, map, and List.
    </p>
    </div>
    </Container>
    </React.Fragment>
    )
  }

}



