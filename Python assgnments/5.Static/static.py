# 1. Define a static variable and access that through a class
class Bakery:
    type = 'cake'                  
    def __init__(self,flavor,price):
        self.flavor = flavor           
        self.price = price 

a = Bakery('Butterscotch Cake', 300)
b = Bakery('Chocolate-Truffle Cake', 250)
 
print(a.type)  
print(b.flavor)    
print(a.price)    



# 2. Define a static variable and access that through a instance
class MyClass:
    static_var = "Hello, World!"
instance = MyClass()

# Access the static variable using an instance of the class
print(instance.static_var)	


							
# 3.Define a static variable and change within the instance          

# 4. Define a static variable and change within the class

class Cake:
    noOfCakes = 0

    @classmethod
    def show(cls):
        print("Inside class method")
        cls.noOfCakes = cls.noOfCakes + 1  ## accessing using clas
        print("No of cakes: ", cls.noOfCakes)
        Cake.noOfCakes = Cake.noOfCakes + 1  ##accessing using class name
        print("No of cakes: ", Cake.noOfCakes)

        c = Cake()
        c.display()
        c.show()
        c.appear()


