import { useState } from 'react';

function Square({value, onSquareClick}) {
	return (
		<button className="square" onClick={onSquareClick}>
			{value}
		</button>
	);
}

let count = 0;
let prevClick = null;
let move;
let winningMove = null;

export default function Board() {
	const [xIsNext, setXIsNext] = useState(true);
	const [squares, setSquares] = useState(Array(9).fill(null));

	function handleClick(i) {
		const nextSquares = squares.slice();
		if (count < 6 && squares[i]) {
			return;
		} 
		if (calculateWinner(squares)) {
			return;
		}
		if (prevClick != null && prevClick === i) {
			prevClick = null;
			move = 'Canceled Selection';
		} else if (prevClick != null && squares[i]) {
			return;
		} else if (count >= 6 && xIsNext) {
			if (nextSquares[i] === 'X' && prevClick === null) {
				winningMove = calculateWinningMoves(i, nextSquares);
				prevClick = i;
				move = 'X is selected at grid number: ' + i;

			} else if (i !== 4 && nextSquares[4] === 'X') {
				if (prevClick !== null && (winningMove === i || prevClick === 4)) {
					nextSquares[i] = 'X';
					nextSquares[prevClick] = null;
					prevClick = null;
					setXIsNext(!xIsNext);
					move = 'X is moved to grid number: ' + i;
				} else {
					prevClick = null;
					move = 'Not a winning move, you must move the center X'
				}
			} else if (prevClick != null && isAdjacent(i, prevClick)) {
				nextSquares[i] = 'X';
				nextSquares[prevClick] = null;
				prevClick = null;
				setXIsNext(!xIsNext);
				move = 'X is moved to grid number: ' + i;
			} else {
				prevClick = null;
				move = 'Invalid Move';
			}
		} else if (count >= 6 && !xIsNext) {
			if (nextSquares[i] === 'O' && prevClick === null) {
				winningMove = calculateWinningMoves(i, nextSquares);
				prevClick = i;
				move = 'O is selected at grid number: ' + i;

			} else if (i !== 4 && nextSquares[4] === 'O') {
				if (prevClick !== null && (winningMove === i || prevClick === 4)) {
					nextSquares[i] = 'O';
					nextSquares[prevClick] = null;
					prevClick = null;
					setXIsNext(!xIsNext);
					move = 'O is moved to grid number: ' + i;
				} else {
					prevClick = null;
					move = 'Not a winning move, you must move the center O'
				}
			} else if (prevClick !== null && isAdjacent(i, prevClick)) {
				nextSquares[i] = 'O';
				nextSquares[prevClick] = null;
				prevClick = null;
				setXIsNext(!xIsNext);
				move = 'O is moved to grid number: ' + i;
			} else {
				prevClick = null;
				move = 'Invalid Move';
			}
		} else {
			if (xIsNext) {
				nextSquares[i] = 'X';
			} else {
				nextSquares[i] = 'O';
			}
			setXIsNext(!xIsNext);
			count++;
		}
		setSquares(nextSquares);
	}
	
	const winner = calculateWinner(squares);
	let status;
	if (winner) {
		status = 'Winner: ' + winner;
	} else {
		if (xIsNext) {
			status = 'Next player: X';
		} else {
			status = 'Next player: O';
		}
	}

	function resetBoard(squares) {
		const empty = squares.slice()
		for (let i = 0; i < squares.length; i++) {
			empty[i] = null;
		}
		prevClick = null;
		count = 0;
		setXIsNext(true);
		setSquares(empty);
	}

	return (
		<>
		<div className="status">{status}</div>
		<div className="board-row">
			<Square value={squares[0]} onSquareClick={() => handleClick(0)} />
			<Square value={squares[1]} onSquareClick={() => handleClick(1)} />
			<Square value={squares[2]} onSquareClick={() => handleClick(2)} />
		</div>
		<div className="board-row">
			<Square value={squares[3]} onSquareClick={() => handleClick(3)} />
			<Square value={squares[4]} onSquareClick={() => handleClick(4)} />
			<Square value={squares[5]} onSquareClick={() => handleClick(5)} />
		</div>
		<div className="board-row">
			<Square value={squares[6]} onSquareClick={() => handleClick(6)} />
			<Square value={squares[7]} onSquareClick={() => handleClick(7)} />
			<Square value={squares[8]} onSquareClick={() => handleClick(8)} />
		</div>
		<button onClick={() => resetBoard(squares)}>Reset Board</button>
		<div className="move">{move}</div>
		</>

	);
}


function isAdjacent(i, prevClick) {
	const adjacent = getAdjacent(prevClick);
	for (let j = 0; j < adjacent.length; j++) {
		if (adjacent[j] === i) {
			return true;
		}
	}
	return false;
}

function getAdjacent(i) {
	const adjacent = [
		[1, 3, 4],
		[0, 2, 3, 4, 5],
		[1, 4, 5],
		[0, 1, 4, 6, 7],
		[0, 1, 2, 3, 5, 6, 7, 8],
		[1, 2, 4, 7, 8],
		[3, 4, 7],
		[3, 4, 5, 6, 8],
		[4, 5, 7]
	];
	return adjacent[i];
}

function calculateWinner(squares) {
	const lines = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],
		[0, 4, 8],
		[2, 4, 6],
  	];
  	for (let i = 0; i < lines.length; i++) {
    	const [a, b, c] = lines[i];
    	if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      		return squares[a];
    	}
  	}
  	return null;
}

function calculateWinningMoves(i, squares) {
	let adjacent = getAdjacent(i);
	for (let j = 0; j < adjacent.length; j++) {
		if (squares[adjacent[j]] === null) {
			const possibleWin = squares.slice();
			possibleWin[adjacent[j]] = possibleWin[i];
			possibleWin[i] = null;
			if (calculateWinner(possibleWin) != null) {
				return adjacent[j];
			}
		} 	
	}
	return null;
}