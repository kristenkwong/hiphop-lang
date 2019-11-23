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

def is_apply_all_expr(expr_str):

    match = re.findall('(?<=apply-all \[)(.*)] to (.*)', expr_str)
    if (len(match) != 1):
        return hiphop_error("ParserError", -1, 'Invalid syntax for `apply-all` expression.')
    match_funcs, match_id = match[0]
    return apply_all_expr(match_funcs, match_id)

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
        else:
            return hiphop_error("InvalidFunctionError", -1, "Function name does not exist.")

class apply_all_expr():

    def __init__(self, apply_funcs, img):

        """
        apply_funcs: string of function calls
        img: img expression
        """

        self.apply_funcs = []

        # Parse the string of functions into lambda functions
        new_funcs = apply_funcs.split(",")
        for new_func in new_funcs:
            self.apply_funcs.append(make_lambda_func(new_func.strip()))

        self.img = img 

    def evaluate(self):

        for func in self.apply_funcs:
            res = func(self.img)
            if (isinstance(res, hiphop_error)):
                return res 

def make_lambda_func(str):
    # From a string representation, creates a lambda function
    # ie. grayscale 50

    func_tokens = str.split(" ")
    funcname, func_args = func_tokens[0], func_tokens[1:]
    print("Making lambda function - funcname: {}, args: {}".format(funcname, func_args))

    if (funcname == "blur"):
        if (len(func_args) != 1):
            return hiphop_error("InvalidFunctionError", -1, "Invalid number of arguments for `blur`")
        return lambda img: blur(img, int(func_args[0]))
    elif (funcname == "grayscale"):
        if (len(func_args) != 0):
            return hiphop_error("InvalidFunctionError", -1, "Invalid number of arguments for `grayscale`")
        return lambda img: blackandwhite(img)
    else:
        return hiphop_error("InvalidFunctionError", -1, "Function name does not exist.")

    
class apply_funcs():

    def __init__(self, funcs_strings):
        """
        Parse string of functions and return list of lambda functions
        funcs_string: list of string representation of functions
        """
        self.apply_funcs = []
        for func_string in funcs_strings:
            self.apply_funcs.append(make_lambda_func(func_string))
        

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

