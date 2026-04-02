#question 6
import clingo 
from clingo.application import Application, clingo_main
from sudoku_board import Sudoku


class Context:

    def __init__(self, board: Sudoku):
        # YOUR CODE HERE
        self.board = board
        
    def initial(self) -> list[clingo.symbol.Symbol]:
        # YOUR CODE HERE
        symbols = []
        
        for (row, col), value in self.board.sudoku.items():
            symbols.append(clingo.Tuple_([clingo.Number(row), clingo.Number(col), clingo.Number(value),]))
            
        return symbols




class SudokuApplication(Application):
    program_name = "sudoku6"

    def main(self, control: clingo.Control, files):
        with open(files[0], "r") as f:
            s = f.read()
        
        board = Sudoku.from_str(s)
        context = Context(board)
        
        control.load("sudoku.lp")
        control.load("sudoku_py.lp")    
        control.ground([("base", [])], context = context)
        control.solve()
      
    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)
           


        
        
        
        
        
        
if __name__ == "__main__":
    clingo_main(SudokuApplication())