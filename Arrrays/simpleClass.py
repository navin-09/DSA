class Person:
    def __init__(self, name, age):      # constructor
        self.name = name
        self.age = age

    def greet(self):                    # instance method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object (instance)
p1 = Person("Alice", 25)

# Call method
p1.greet()
