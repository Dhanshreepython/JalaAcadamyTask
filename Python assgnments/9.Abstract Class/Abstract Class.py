# 1. Create an abstract class with abstract and non-abstract methods.

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        print("abstract method")

    def non_abstract_method(self):
        print("Non-abstract method")

class ConcreteClass(AbstractClass): #a class that has a definition for all its methods and has no abstract method.
    def abstract_method(self):
        print("Concrete implementation of abstract method")

# Creating an instance of the ConcreteClass
obj = ConcreteClass()

# Calling abstract and non-abstract methods
obj.abstract_method()
obj.non_abstract_method()



# Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methodsx
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        print("abstract method")

    def non_abstract_method(self):
        print("Non-abstract method")


class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Concrete implementation of abstract method")


class SubClass(AbstractClass):
    def abstract_method(self):
        print("Concrete implementation of abstract method in SubClass")


#instance of ConcreteClass
concrete_obj = ConcreteClass()
concrete_obj.abstract_method()
concrete_obj.non_abstract_method()

# instance of SubClass
sub_obj = SubClass()
sub_obj.abstract_method()
sub_obj.non_abstract_method()



# 3. Create an instance for the child class in child class and call abstract methods
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass


class SubClass(AbstractClass):
    def abstract_method(self):
        print("Concrete implementation of abstract method in SubClass")

    def call_abstract_method(self):
        self.abstract_method()


#instance of SubClass within the SubClass itself
sub_obj = SubClass()
sub_obj.call_abstract_method()



# 4. Create an instance for the child class in child class and call non-abstract methods
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("Non-abstract method")


class SubClass(AbstractClass):
    def abstract_method(self):
        print("Concrete implementation of abstract method in SubClass")

    def call_non_abstract_method(self):
        self.non_abstract_method()


#instance of SubClass within the SubClass itself
sub_obj = SubClass()
sub_obj.call_non_abstract_method()
