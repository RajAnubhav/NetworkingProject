# class ParentClass:
#     def __init__(self):
#         self.value = 10
#
#     def some_function(self):
#         return self.value
#
# class ChildClass(ParentClass):
#     def __init__(self):
#         super().__init__()  # Invoke the parent class constructor
#
#     def some_function(self):
#         parent_value = super().some_function()  # Invoke the parent class function
#         return parent_value
#
# # Create an instance of the child class
# child_obj = ChildClass()
#
# # Call the overridden function in the child class
# child_value = child_obj.some_function()
# print(child_value)  # Output: 10

class ParentClass:
    def __init__(self):
        self.value = 10

    def some_function(self):
        return self.value

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Invoke the parent class constructor

    def some_function(self):
        parent_value = ParentClass.some_function(self)  # Invoke parent class method
        return parent_value

# Create an instance of the child class
child_obj = ChildClass()

# Call the overridden function in the child class
child_value = child_obj.some_function()
print(child_value)  # Output: 10

print(isinstance(child_value, type(child_obj.value)))
