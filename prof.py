class person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class professor(person):
    
    def isprofessor(self):
        return f"{self.name} is a professor"
    
sir=professor("balaji",30)

print(sir.isprofessor())


class superclass1:
    num1=3