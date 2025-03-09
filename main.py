import os
import sys
import random


def my_function(arg1, arg2):
    """
    This is a very poorly formatted function with style issues.

    Args:
        arg1:  A random number.
        arg2: A   string.
    """
    if (arg1 > 10):
        print("arg1 is greater than 10")
        result = arg1 + 5
    else:
        print("arg1 is not greater than 10")
        result = arg1 - 5
    if arg2 == "hello":
        print ("hello there")

    
    return result
    



class MyClass:
    def __init__(self, value):
        self.my_value = value

    def   do_something  (self):
        if self.my_value > 5:
            print("Value is big")
        else:
            print("Value is small")


if __name__ == "__main__":
    value1 = random.randint(0,20)
    value2="hello"
    
    my_function( value1,value2 )
    instance = MyClass( 7)
    instance.do_something()
    
    x= 10
    y=20
    if x <y :
        print("x is smaller than y")

# This code has many style issues that are common in poorly written code:
# - Inconsistent indentation (mixed spaces and tabs)
# - Missing spaces around operators
# - Inconsistent spacing around function definitions and calls
# - Long lines exceeding the recommended length
# - Unnecessary parentheses in if statements
# - Inconsistent use of whitespace
# - Inconsistent use of new lines
# - No comments
# - Multiple line in the same line
# - Extra empty lines
# - extra spaces in class methods
