from unicodedata import name


class Dog :  #class name must be in capital
    def __init__(self, name, colour,speed,tail,height,nails):
        self.name=name
        self.colour=colour
        self.speed=speed
        self.tail=tail
        self.height=height
        self.nails=nails
        self.energe=1
    def manyun (self):
        return (f"this is dog call { self.name} is {self.colour} and have {self.tail} with height of {self.height} and {self.nails} usually run at the speed of {self.speed} .")
    def exercise(self):
        self.energe = self.energe+1
         # __init__() should return None, not 'type'
Nairobi_dogs= Dog("Simba", "black","400m per hour","long tails","500m","long nails") # new is an object same as Instance
USA_DOGS= Dog("Simba", "green","90m per hour","long tails","500m","long nails") # new is an object same as Instance
Home_dogs= Dog("Simba", "blue","490m per hour","long tails","500m","long nails") # new is an object same as Instance
KKK_securitydogs= Dog("Simba", "yellow","300m per hour","long tails","500m","long nails") # new is an object same as Instance
 
print(f"The dog name is {USA_DOGS.name} and is colour {USA_DOGS.colour}")
print(Nairobi_dogs.manyun())
print(f"The dog name is {KKK_securitydogs.name} and is colour {KKK_securitydogs.colour}")
print(f"The dog name is {KKK_securitydogs.energe} and is colour {USA_DOGS.colour}")


#class is a template for creating objects i.e It allows to create many dogs
