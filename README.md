# Concepts in Object Oriented Programming

## Class

- A template(blueprint) for the creation of an object


### `__init__` (initializer)

- Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created

### Attribute (Parameter)

- Descriptions of properties of the object (e.g. Name, Age, etc.)
- Instance attribute (first name)
- Class-level attribute (WSU as a school)

### Methods (Actions)
- Instance Method
    - Method that can be performed on the object
- Class Method
    - Allows us to create and modify class level data
- Static Method
    - Does not have access to class or instance attributes but performs action within the class
- Magic
    - Reserved methods that perform a specific task e.g. `__str__`


## Inhertiance
- Inheritance allows us to define a class that inherits all the methods and properties from another class.
- Parent Class (Student)
- Child Class (Graduate Student)


## Polymorphism
- methods/functions/operators with the same name that can be executed on many objects or classes.