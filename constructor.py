#constructing constructors:
class Animal:  
    def __init__(self, name, type):  
        self.type = type  
        self.name = name  
  
    def display(self):  
        print("type: %s \nName: %s" % (self.type, self.name))  
  
  
pet1 = Animal("Goofy","Dog")  
pet2 = Animal("Miami", "Cat")  

pet1.display()  
pet2.display() 

