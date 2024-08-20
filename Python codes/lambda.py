# What Are Lambda Functions?
# Lambda functions, also known as anonymous functions, 
# are like magical one-liners in Python. They’re concise, 
# mysterious, and don’t require a formal name. Picture them 
# as the secret agents of the function world—here for a quick 
# mission and then vanishing into thin air.

# Syntax
# lambda arguments: expression

# Regular function to find the average of three numbers
def average(x, y, z):
    return (x + y + z) / 3

# Equivalent lambda function
average_lambda = lambda x,y,z : (x+y+z)/3

# Usage 
print(average_lambda(3, 4, 5))  # Output: 4.0
