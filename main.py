from hiphopparse import Parser
import sys
from hiphoperrors import hiphop_error, hiphop_eval_error

def main():

    parser = Parser()

    # count number of arguments
    if (len(sys.argv) == 2):
        filename = sys.argv[1]
        # print("Interpreting HIPHOP program with the filename: {}".format(filename))
        try:
            parser.parse(filename)
        except hiphop_error as e:
            print("There was a problem parsing the file on line {}: {}".format(e.line_num, e.msg))
        except hiphop_eval_error as e:
            print("There was a problem with evaluating an expression: {}".format(e.msg))
    else:
        print("Usage: `python main.py <filename>`")

if __name__ == "__main__":
    main()
