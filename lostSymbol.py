
'''Class to create a Symbol and its location'''
class Symbol:
    def __init__(self, name, look, location):
        self.name = name
        self.look = look
        self.location = location
    
    def __str__(self):
        return f"Symbol Name: {self.name}\nSymbol Look: {self.look}\nLocation: {self.location}"

    def __repr__(self):
        return f"Symbol Name: {self.name}\n Symbol Look: {self.look}\n Location: {self.location}"

'''Calling class to print out symbol'''
print(Symbol("Alpha", "A", (12,34)).__doc__);