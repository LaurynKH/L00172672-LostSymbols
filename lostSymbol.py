
'''Class to create a Symbol and its location'''
class Symbol:
    def __init__(self, name, look, location):
       '''Name of Symbol'''
        self.name = name
        '''Look of the Symbol'''
        self.look = look
        '''Location of the Symbol'''
        self.location = location
    
    '''To string'''
    def __str__(self):
        return f"Symbol(Name: {self.name}, Look: {self.look}, Location: {self.location})"

    '''Repr'''
    def __repr__(self):
        return f"Symbol(Name: {self.name!r}, Look: {self.look!r}, Location: {self.location!r})"


'''Calling class to print out symbol'''
print(Symbol("Alpha", "A", (12,34)).__doc__);
