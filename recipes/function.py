
# create my own function and call it
# https://www.tutorialspoint.com/python/python_functions.htm

# ==================================================
# simple function call

def myfunction(x, y):
    z = x + y
    return z

myvalue = myfunction(3, 4)
print(myvalue)

myvalue = myfunction(5, 3)
print(myvalue)

print("-------------------")

# ==================================================
# using keywork arguments

def calc_cost(price, quantity=1):
    cost = price * quantity
    return cost

bill = calc_cost(price=10, quantity=56)
print(bill)

# demonstrate default value for quantity
bill = calc_cost(price=25)
print(bill)
