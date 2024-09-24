## About The Project

This project is an exploration of solving Sudoku puzzles using a heuristic approach that mimics human strategies.
A common computer science principle used to solve sudoku is backtracking. When confronted with two options, pick one and see if it could
result in a solution, if not backtrack to where you made this split.
For a human this is really annoying to do, because if that branch 'fails' i.e. you arrive at a contradiction you have to
revert back to that point where you branched out. I like to solve my sudokus in one shot.

In this repository, we approach it in a simpler manner where we solve each sudoku as a human would, by putting a digit down only if
no other digits can go in this cell or if that digit can only go here.

The code involves representing the Sudoku board as a `Table` class, where each individual cell is an instance of the `Cell` class.
I did this project as a way to make a long flight interesting, so goal is to have fun with a puzzle that has fascinated me as a kid while applying and practicing principles of good software engineering.


## Getting Started

This python project uses widely spread Python libraries, so you can simply run the main.py file to execute the code.
I added my versions below. 

You might need:
- pandas (v2.2.2)
- numpy (v2.1.1)

## Data

We selected a few simple examples to get started, see in the sudoku_files folder.
1 million examples were then added from this Kaggle page: https://www.kaggle.com/datasets/bryanpark/sudoku/code.
For simplicity it was also added into this repo so you don't have to download this.

## Results

Our very simple approach, not even using backtracking (Like a human would), is actually capable of solving all of those puzzles!

## Roadmap

- [x] Implement simple solving
- [x] Add Additional Examples
- [ ] Implement backtracking (Maybe ?)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
