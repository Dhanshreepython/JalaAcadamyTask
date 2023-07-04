# 1. A, B and C are classes# define a superclass


# define a superclass
class super_classA:
   pass

class sub_classB(super_classA):
   pass


class subclassC(sub_classB):
   pass



# 2.Create three methods in each class, 2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C

class A:
    def method_a1(self):
        # Specific method for class A
        pass

    def method_a2(self):
        # Specific method for class A
        pass

    def override_method(self):
        # Override method implemented in class A
        pass


class B:
    def method_b1(self):
        # Specific method for class B
        pass

    def method_b2(self):
        # Specific method for class B
        pass

    def override_method(self):
        # Override method implemented in class B
        pass


class C:
    def method_c1(self):
        # Specific method for class C
        pass

    def method_c2(self):
        # Specific method for class C
        pass

    def override_method(self):
        # Override method implemented in class C
        pass



# 3.Create a class with main method. Create an object for each class A, B and C in main method and call every method of each class using its own object/instance.
class MainClass:
    def main(self):
        # Create objects for classes A, B, and C
        object_a = A()
        object_b = B()
        object_c = C()

        object_a.method_a1()
        object_a.method_a2()
        object_a.override_method()

        object_b.method_b1()
        object_b.method_b2()
        object_b.override_method()

        object_c.method_c1()
        object_c.method_c2()
        object_c.override_method()


class A:
    def method_a1(self):
        print("Method A1 of class A")

    def method_a2(self):
        print("Method A2 of class A")

    def override_method(self):
        print("Override method of class A")


class B:
    def method_b1(self):
        print("Method B1 of class B")

    def method_b2(self):
        print("Method B2 of class B")

    def override_method(self):
        print("Override method of class B")


class C:
    def method_c1(self):
        print("Method C1 of class C")

    def method_c2(self):
        print("Method C2 of class C")

    def override_method(self):
        print("Override method of class C")


# instance of the MainClass and call the main method
main_obj = MainClass()
main_obj.main()



# Call an overridden method with super class reference to B and C class’s objects

class A:
    def override_method(self):
        print("Override method of class A")


class B(A):
    def override_method(self):
        print("Override method of class B")


class C(A):
    def override_method(self):
        print("Override method of class C")


# Create objects for classes B and C
obj_b = B()
obj_c = C()

# Call overridden method using superclass reference
super(B, obj_b).override_method()
super(C, obj_c).override_method()



# Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members

# In Python, instance variables are not directly overridden like methods in the case of runtime polymorphism. However, you can achieve similar behavior by using property decorators and accessing the instance variables through getter and setter methods.
class A:
    def __init__(self):
        self.data_member = "Data member of class A"

    @property
    def data_member(self):
        return self._data_member

    @data_member.setter
    def data_member(self, value):
        self._data_member = value


class B(A):
    def __init__(self):
        super().__init__()
        self.data_member = "Data member of class B"


class C(A):
    def __init__(self):
        super().__init__()
        self.data_member = "Data member of class C"


# Create objects for classes B and C
obj_b = B()
obj_c = C()

# Access data member using superclass reference
print(obj_b.data_member)  
print(obj_c.data_member) 




