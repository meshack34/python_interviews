from unicodedata import name


class Dog :  #class name must be in capital
    def __init__(self, name, colour,speed,tail,height,nails):
        self.name=name
        self.colour=colour
        self.speed=speed
        self.tail=tail
        self.height=height
        self.nails=nails
         # __init__() should return None, not 'type'
Nairobi_dogs= Dog("Simba", "black","400 per hour","long tails","500m","long nails") # new is an object same as Instance
USA_DOGS= Dog("Simba", "black","400 per hour","long tails","500m","long nails") # new is an object same as Instance
Home_dogs= Dog("Simba", "black","400 per hour","long tails","500m","long nails") # new is an object same as Instance
KKK_securitydogs= Dog("Simba", "black","400 per hour","long tails","500m","long nails") # new is an object same as Instance
def manyun (y):
    return (f"this is dog call { y.name} is {y.colour} and is {y.speed}{y.tail}{y.height}{y.nails}")

cool= manyun(Nairobi_dogs)  
print(cool)   
print(f"The dog name is {USA_DOGS.name} and is colour {USA_DOGS.colour}")


#class is a template for creating objects i.e It allows to create many dogs
