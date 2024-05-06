from math import pi

# Basic operators
def add(x: str, y: str) -> float:
    '''
    Method to get the sum of two numbers.
    
    Parameters:
    x -- First number
    y -- Second number.
    '''
    
    if '.' in x:
        x = float(x)
    else:
        x = int(x)
    if '.' in y:
        y = float(y)
    else:
        y = int(y)

    return x + y


def subtract(x: str, y: str) -> float:
    '''
    Method to get the difference of two numbers.
    
    Parameters:
    x -- First number
    y -- Second number.
    '''
    
    if '.' in x:
        x = float(x)
    else:
        x = int(x)
    if '.' in y:
        y = float(y)
    else:
        y = int(y)

    return x - y


def divide(x: str, y: str) -> float:
    '''
    Method to get the quotient of two numbers.
    
    Parameters:
    x -- First number
    y -- Second number.
    '''
    
    if '.' in x:
        x = float(x)
    else:
        x = int(x)
    if '.' in y:
        y = float(y)
    else:
        y = int(y)

    return x / y
    

def squared(x: str, y: str) -> float:
    '''
    Method to get the squared product of two numbers.
    
    Parameters:
    x -- First number
    y -- Second number.
    '''
    
    if '.' in x:
        x = float(x)
    else:
        x = int(x)
    if '.' in y:
        y = float(y)
    else:
        y = int(y)

    return x ** y


def multiply(x: str, y: str) -> float:
    '''
    Method to get the product of two numbers.
    
    Parameters:
    x -- First number
    y -- Second number.
    '''
    
    if '.' in x:
        x = float(x)
    else:
        x = int(x)
    if '.' in y:
        y = float(y)
    else:
        y = int(y)

    return x * y


# Mode: Area
def circle(radius: str) -> float:
    '''
    Method to get the area of a circle.
    
    Parameters:
    radius -- Radius of a circle.
    '''
    
    radius = float(radius)
    if radius <= 0:
        raise TypeError
    else:
        return pi * radius ** 2


def square(length):
    length = float(length)
    if length <= 0:
        raise TypeError
    else:
        return length ** 2


def rectangle(width, height):
    width, height = float(width), float(height)
    if width <= 0 or height <= 0:
        raise TypeError
    else:
        return width * height


def triangle(base, height):
    base, height = float(base), float(height)
    if base <= 0 or height <= 0:
        raise TypeError
    else:
        return base * height / 2