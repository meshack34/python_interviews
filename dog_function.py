from unicodedata import name


class Dog :  #class name must be in capital
    def __init__(self, name, colour):
        self.name=name
        self.colour=colour
         # __init__() should return None, not 'type'
new= Dog("Simba", "black") # new is an object same as Instance
def manyun (y):
    return (f"this is dog call { y.name} is {y.colour}")
cool= manyun(new)
print(cool)       
print(f"The dog name is {new.name} and is colour {new.colour}")