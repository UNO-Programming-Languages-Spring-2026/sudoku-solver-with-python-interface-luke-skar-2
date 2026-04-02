
import clingo 
from clingo.application import Application, clingo_main

class SudokuApplication(Application):
    program_name = "sudoku1"
    
    
    def main(self, control: clingo.Control, files):
        control.load("sudoku.lp")
        
        for file_name in files:
            control.load(file_name)
            
        control.ground([("base",[])])
        control.solve()
        
        
if __name__ == "__main__":
    clingo_main(clingo_main(SudokuApplication()))
