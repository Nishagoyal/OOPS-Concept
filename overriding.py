#overriding:

class Class1:  
    def speak(self):  
        print("speaking")  
class Class2(Class1):  
    def speak(self):  
        print("listening")  
person = Class2()  
person.speak()  