class HelloProgram:
    print("Hello Welcome")


    def __init__(self,name):
        self.name=name
        print("Name"+name)


    def add(self,a,b):
        c = a+b
        return c

    def multiply(self,a,b):
        c=a*b
        return c

    def divide(self,a,b):
        c=a/b
        return c

    def modules(self,a,b):
        c=a%b
        return c
    def remainder(self,a,b):
        c=a//b
        return c
    

h= HelloProgram("Srivalle")
print(h.add(3,5))
print(h.multiply(12,4))
print(h.divide(90,10))
print(h.modules(35,4))
print(h.remainder(45,4))
      

    
        
    
