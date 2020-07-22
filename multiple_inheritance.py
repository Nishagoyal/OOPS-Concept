
#Multiple inheritance
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print("summation",d.Summation(10,20))  
print("multiplication",d.Multiplication(10,20))  
print("divide",d.Divide(10,20))

# to check if sub class or not
# True if class 1 is subclass 2 
# else false
print("Derived is the subclass of Calculation2",issubclass(Derived,Calculation2))  
print("Derived is the subclass of Calculation2",issubclass(Calculation1,Calculation2)) 


#to check if an object of the given class or not
print("object d is an instance of class Derived:",isinstance(d,Derived))  
