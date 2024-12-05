"""   This class represents the Lost Symbol in the game world.
    
    Attributes:
        name (str): The name of the symbol.
        location (tuple): The location of the symbol (x, y).
        is_found (bool): Whether the symbol has been found or not.
"""
class Symbol:
    def __init__(self, name, look, location):
        """
        Initializes the LostSymbol object with a name and location.
        
        Args:
            name (str): The name of the symbol.
            look(char): look of symbol eg. & or A
            location (tuple): The location of the symbol as a tuple (x, y).
        """
        self.name = name
        self.look = look
        self.location = location

    '''Repr '''
    def __repr__(self):
        return f"Symbol(Name: {self.name!r}, Look: {self.look!r}, Location: {self.location!r})"

