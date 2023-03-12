import React, { Component } from 'react';
import './Instructions.css';
import Trie_example from './Trie_example.svg.png';
import knightmoves from './knightmoves.png';
export default class Instructions extends Component {

  render() {
    return(
    <React.Fragment>
    <div class="card-body">
    <h2>Welcome to the Knight's tour!</h2>
    <p><em>
    The Knights' Tour is an exercise in computing science, algorithms and it's just a fun toy to play with! In essence, it is a combination of a Trie string walker, and a Chess player that only knows how to move knights around.
    </em>
    </p>
    <p>
    The algorithm will efficiently search through a space-separated list of words, organised into a <a class="link" href="https://en.wikipedia.org/wiki/Trie" target="_blank">Trie structure</a> (aka a Radix Tree): These words will be matched against the characters stored inside an 8x8 matrix that represents a chess board. For each position on the board, Knight's tour will visit it first (only if its character matches strings in the Trie struct):
    </p>
    <h3>A <a class="link" href="https://en.wikipedia.org/wiki/Trie" target="_blank">Trie</a> Struct is a form of Radix tree:</h3>
    <img src={Trie_example} className="trie-example" alt="Trie Example" />

    <p>
    Then, Knights tour will recursively descend down the tree of possible moves that each individual square visited presents; with the constraint that it only visits squares that contain characters that -are- found in the next node of the Trie in order to find the longest possible string contained in the Trie, that is possible with the characters specified in the matrix that represents the chess board:
    </p>
    <img src={knightmoves} className="trie-example" alt="Trie Example" />

    <p>
    In order to keep the algorithm fast, efficient and without doing a lot of deep recursion, the solution was implemented using a recursive chess walker defined in "run_knights_tour" and "get_moves". The total Big O execution time of the Knights tour is O(n), where n is the length of the maximum string. (We could be pedantic and say it is O(64n) because of the 8x8 board, but this is a worst-case scenario; and the constant matrix size will not dominate the Trie size.)
    </p>
    </div>
    </React.Fragment>
    )
  }

}



