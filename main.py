from hiphopparse import Parser
from hiphopinterp import Interpreter
import sys 

class var_dict():
    """
    Keeps track of ids holding images within the program.
    """

    def __init__(self):

        self.map = {}

    def add_var(self, id, img):

        self.map[id] = img 

    def get_var(self, id):

        return self.map[id]

def main():

    interp = Interpreter()
    parser = Parser(interp)
    
    # count number of arguments
    if (len(sys.argv) == 2):
        filename = sys.argv[1]
        print("Interpreting HIPHOP program with the filename: {}".format(filename))
        parser.parse(filename)
    else:
        print("Usage: `python main.py <filename>`")

if __name__ == "__main__":
    main()