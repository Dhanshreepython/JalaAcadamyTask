# File: AnotherClass.py

from myclass import MyClass

class AnotherClass:
    def access_public_members(self, obj):
        # Access public field from MyClass instance
        print(obj.public_field)

        # Call public method from MyClass instance
        obj.public_method()
