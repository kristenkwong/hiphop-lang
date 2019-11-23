import re 
from core import *

"""
<HHE> ::= apply <func> <args> to <id>
        | open "<filename>" as <id>
        | save <id> as "filename>"
        | <id>
        | <num>

<args> ::= <arg>
         | <arg> <args>
         | 

<arg> ::= NUMBER

<id> ::= STRING 
"""

def is_open_expr(expr_str):
    # For one line of the program, if valid program return object,
    # otherwise False 

    match_filename = re.findall('(?<=open ")(.*)(?=" as)', expr_str)
    match_id = re.findall('(?<=open ")*(?<=" as )(.*)$', expr_str)
    if (len(match_filename) != 1 or len(match_id) != 1):
        return hiphop_error("ParserError", -1, 'Invalid syntax for `open` expression.')
    else:
        return open_expr(match_filename[0], match_id[0])

def is_save_expr(expr_str):

    match_id = re.findall('(?<=save )(.*)(?= as)', expr_str)
    match_filename = re.findall('(?<=save ).*(?<= as ")(.*)"', expr_str)
    print("filename: {}; id: {}".format(match_filename[0], match_id[0]))
    if (len(match_filename) != 1 or len(match_id) != 1):
        return hiphop_error("ParserError", -1, 'Invalid syntax for `save` expression.')
    else:
        return save_expr(match_id[0], match_filename[0])

def is_apply_expr(expr_str):

    match = re.findall('(?<=apply )(.*)( to )(.*)', expr_str)
    if (len(match) != 1):
        return hiphop_error("ParserError", -1, 'Invalid syntax for `apply` expression.')
    match_func, _, match_id = match[0]
    match_function= match_func.split()
    match_funcname, match_args = match_function[0], match_function[1:]
    print("funcname: {}; args: {}; id: {}".format(match_funcname, match_args, match_id))
    return apply_expr(match_funcname, match_args, match_id)

class open_expr():

    def __init__(self, filename, id):

        self.filename = filename 
        self.id = id 

    def evaluate(self):
        openfile(self.filename, self.id)


class save_expr():

    def __init__(self, id, filename):

        self.id = id 
        self.filename = filename

    def evaluate(self):
        savefile(self.id, self.filename)

class apply_expr():

    def __init__(self, funcname, args, img):

        """
        funcname: function to call when expression is evaluated
        args: list of arguments going into the function 
        img: img expression
        """

        self.funcname = funcname 
        self.args = args 
        self.img = img 

    def evaluate(self):

        if (self.funcname == "blur"):
            if (len(self.args) != 1):
                return hiphop_error("InvalidFunctionError", -1, "Invalid number of arguments for `blur`")
            blur(self.img, int(self.args[0]))
        elif (self.funcname == "grayscale"):
            if (len(self.args) != 0):
                return hiphop_error("InvalidFunctionError", -1, "Invalid number of arguments for `grayscale`")
            blackandwhite(self.img)
        elif (self.funcname == "filtercolor"):
            if (len(self.args) != 6):
                return hiphop_error("InvalidFunctionError", -1, "Invalid number of arguments for `filtercolor lowR lowG lowB highR highG highB`")
            filtercolor(self.img, int(self.args[0]), int(self.args[1]), int(self.args[2]), 
                                  int(self.args[3]), int(self.args[4]), int(self.args[5]))
        else:
            return hiphop_error("InvalidFunctionError", -1, "Function name does not exist.")

class identifier():

    def __init__(self, boundvar):

        self.boundvar = boundvar 

    def get_value(self):

        return self.boundvar

class hiphop_error():

    def __init__(self, error_type, line_num, error_msg):

        self.error_type = error_type
        self.line_num = line_num
        self.error_msg = error_msg

    def printError(self):
        print("{} (line {}): {}".format(self.error_type, self.line_num, self.error_msg))

