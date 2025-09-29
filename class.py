# 1. Define the class (the blueprint)
class Dog:
    """
    This class represents a dog.
    """

    # 2. The __init__ method (the constructor)
    # This method runs automatically when you create a new Dog object.
    def __init__(self, name, age):
        # 3. Attributes (the data for each object)
        # 'self' refers to the specific instance of the object being created.
        self.name = name
        self.age = age
        print(f"A new dog named {self.name} has been created!")

    # 4. A method (a function that belongs to the class)
    def bark(self):
        """Makes the dog bark."""
        return f"{self.name} says: Woof! 🐾"

    # Another method that uses the object's attributes
    def get_info(self):
        """Returns a string with the dog's information."""
        return f"{self.name} is {self.age} years old."

# --- Using the class to create objects ---

# 5. Create objects (instances of the Dog class)
# This calls the __init__ method for each dog.
dog1 = Dog("Buddy", 4)
dog2 = Dog("Lucy", 2)

print("-" * 20)

# 6. Access attributes and call methods for each object
# Accessing attributes
print(f"Dog 1's name is: {dog1.name}")
print(f"Dog 2's age is: {dog2.age}")

print("-" * 20)

# Calling methods
print(dog1.bark())
print(dog2.get_info())