# 1. Write two methods with the same name but different number of parameters of same type and call the methods

class MyClass:
    def method_with_one_parameter(self, param):
        print("Method with one parameter:", param)

    def method_with_two_parameters(self, param1, param2):
        print("Method with two parameters:", param1, param2)


# Create an instance of MyClass
obj = MyClass()

# Call the methods with different numbers of parameters
obj.method_with_one_parameter("Hello")
obj.method_with_two_parameters("Hello", "python world")




# 2. Write two methods with the same name but different number of parameters of different data type and call the methods

class MyClass:
    def method_with_parameters(self, param1, param2=None):
        if param2 is None:
            # Method called with one parameter
            print("Method with one parameter:", param1)
        else:
            # Method called with two parameters
            print("Method with two parameters:", param1, param2)

    def method_with_parameters(self, param1, param2, param3):
        # Method called with three parameters
        print("Method with three parameters:", param1, param2, param3)


# instance of MyClass
obj = MyClass()

obj.method_with_parameters("Hello")
obj.method_with_parameters("Hello", 10)
obj.method_with_parameters("Hello", 10, True)



# 3. Write two methods with the same name and same number of parameters of same type

class MyClass:
    def my_method(self, param):
        print("First method:", param)

    def my_method(self, param):
        print("Second method:", param)


obj = MyClass()

obj.my_method("Hello")



