from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        
        for row in range (1, 10):
            row_values = []
            
            for col in range (1, 10):
                row_values.append(str(self.sudoku[(row, col)]))
            s += " ".join(row_values[0:3]) + "  " + \
                 " ".join(row_values[3:6]) + "  " + \
                 " ".join(row_values[6:9])
            if row != 9:
                s += "\n"
            if row == 3 or row == 6:
                s += "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        rows = [line for line in s.splitlines() if line.strip() != ""]
        
        for row_index, line in enumerate(rows, start = 1):
            values = line.split()
            for col_index, value in enumerate(values, start = 1):
                if value != "-":
                    sudoku[(row_index, col_index)] = int(value)
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        for sym in model.symbols( shown = True):
            row = sym.arguments[0].number
            col = sym.arguments[1].number
            val = sym.arguments[2].number
            sudoku[(row, col)] = val
        return cls(sudoku)
