# Write a class with a default constructor, one argument constructor and two argument constructors. Instantiate the class to call all the constructors of that class from a main class

class Class1:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor called")
            self.value1 = 0
            self.value2 = 0
        elif arg2 is None:
            print("One-Argument Constructor called")
            self.value1 = arg1
            self.value2 = 0
        else:
            print("Two-Argument Constructor called")
            self.value1 = arg1
            self.value2 = arg2


if __name__ == "__main__":
    obj1 = Class1()
    obj2 = Class1(10)
    obj3 = Class1(20, 30)



# 2. Call the constructors(both default and argument constructors) of super class from a child class


class ParentClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("ParentClass Default Constructor called")
            self.value1 = 0
            self.value2 = 0
        else:
            print("ParentClass Parameterized Constructor called")
            self.value1 = arg1
            self.value2 = arg2


class ChildClass(ParentClass):
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("ChildClass Default Constructor called")
            super().__init__()  # Call the default constructor of the parent class
        else:
            print("ChildClass Parameterized Constructor called")
            super().__init__(arg1, arg2)  # Call the parameterized constructor of the parent class


if __name__ == "__main__":
    # Instantiate ChildClass to call constructors
    obj1 = ChildClass()
    obj2 = ChildClass(10, 20)



# 3. Apply private, public, protected and default access modifiers to the constructor

class MyClass:
    def __init__(self):
        # Public constructor
        pass


class MyClass:
    def __init__(self):
        # Private constructor (convention, not enforced)
        pass

    def _private_method(self):
        # Private method
        pass


class MyClass:
    def _protected_method(self):
        # Protected method
        pass

    def _protected_constructor(self):
        # Protected constructor (convention, not enforced)
        pass



class MyClass:
    def __init__(self):
        # Default constructor
        pass




# 4. Write a program which illustrates the concept of attributes of a constructor.

class MyClass:
    def __init__(self, arg1, arg2):
        self.attribute1 = arg1
        self.attribute2 = arg2

    def display_attributes(self):
        print("Attribute 1:", self.attribute1)
        print("Attribute 2:", self.attribute2)


#instance of MyClass
obj = MyClass("Value 1", "Value 2")
obj.display_attributes()
