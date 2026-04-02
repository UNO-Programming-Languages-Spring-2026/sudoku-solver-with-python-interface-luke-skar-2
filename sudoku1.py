#Final answer part A
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
     #part B   
    def print_model(self, model, printer):
        atoms = model.symbols(shown = True)
        atoms = sorted(atoms, key = str)
        print(" ".join(str(atom) for atom in atoms))    
        
        
if __name__ == "__main__":
    clingo_main(SudokuApplication())