#Multi-Level inheritance
class Parent:  
    def speak(self):  
        print("Hi! This is base-class")  
 
class Child(Parent):  
    def answer(self):  
        print("Hey , This is derived-class")  
person = Child()  
person.answer()  
person.speak()  
