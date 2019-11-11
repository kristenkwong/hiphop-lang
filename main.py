from hiphopparse import Parser
from hiphopinterp import Interpreter
import sys 

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