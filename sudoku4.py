#question4
import clingo 
from clingo.application import Application, clingo_main
from sudoku_board import Sudoku

class SudokuApplication(Application):
    program_name = "sudoku4"

    def main(self, control: clingo.Control, files):
        control.load("sudoku.lp")
        
        for file_name in files:
            control.load(file_name)
            
        control.ground([("base",[])])
        control.solve()
      
    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)
           
        
        
if __name__ == "__main__":
    clingo_main(SudokuApplication())