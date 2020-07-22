#Creating an instance of the class

class animal:    
    id = 10   
    name = "Dog"    
    def display (self):    
        print("ID: %d \nName: %s"%(self.id,self.name))    
pet = animal()    
pet.display() 