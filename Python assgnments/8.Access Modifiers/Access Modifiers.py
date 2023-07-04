# 1. Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. Call the private method in main method.

class MyClass:   #private field
    def __init__(self):
        self._private_field = "Private Field"

    def _private_method(self):
        print("Private Method")

    def main(self):
        # Print private field
        print(self._private_field)

        # Call private method
        self._private_method()


class SubClass(MyClass):
    def access_private_members(self):
        # Access private field from superclass
        print(self._private_field)

        # Call private method from superclass
        self._private_method()


#  instance of MyClass
my_object = MyClass()

my_object.main()
sub_object = SubClass()
# Access private members from SubClass
sub_object.access_private_members()


#

