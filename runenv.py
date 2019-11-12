# Everything responsible for saving the state of the program
# such as all identifiers

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

saved_vars = var_dict()