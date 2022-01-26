import math

# A function that finds all appearances of a substring in a string.
def find_all(string, substring, start):
    index = string.find(substring, start)
    if index == -1:
        return []
    else:
        return [index] + find_all(string, substring, index + len(substring))

# Gets the parameters needed from the user.
while True:
    print("use default graph size? y/n (79 by 19)")
    inp = input()
    if inp == "y":
        graph_w = 80 - 1
        graph_h = 20 - 1
        break
    elif inp == "n":
        print("enter graph width (in characters): ")
        while True:
            try:
                graph_w = int(input())
            except ValueError:
                print("graph width must be a whole number")
                continue
            if graph_w <= 0:
                print("graph width must be positive")
                continue
            break
        print("enter graph height: ")
        while True:
            try:
                graph_h = int(input())
            except ValueError:
                print("graph height must be a whole number")
                continue
            if graph_h <= 0:
                print("graph height must be positive")
                continue
            break
        break
    else:
        print("incorrect input")
    

while True:
    print("use default bounds for graph? y/n (-1 to 1 on both x and y)")
    inp = input()
    if inp == "y":
        upper_x = 1 
        lower_x = -1 
        upper_y = 1 
        lower_y = -1
        break
    elif inp == "n":
        print("enter lower x bound: ")
        while True:
            try:
                lower_x = float(input())
            except ValueError:
                print("lower bound must be a number")
                continue
            break
        print("enter upper x bound: ")
        while True:
            try:
                upper_x = float(input())
            except ValueError:
                print("upper bound must be a number")
                continue
            if upper_x <= lower_x:
                print("upper bound must be higher than the lower bound")
                continue
            break
        print("enter lower y bound: ")
        while True:
            try:
                lower_y = float(input())
            except ValueError:
                print("lower bound must be a number")
                continue
            break
        print("enter upper y bound: ")
        while True:
            try:
                upper_y = float(input())
            except ValueError:
                print("upper bound must be a number")
                continue
            if upper_y <= lower_y:
                print("upper bound must be higher than the lower bound")
                continue
            break
        break
    else:
        print("incorrect input.")

'''
Creates an list of size graph_w,
with values from lower_x to upper_x,
and an exact 0 where its supposed to be.
(trust the math)
Besides 0, the values are not exact,
but for the sake of visualisation they're good.
'''
width = upper_x - lower_x
if lower_x == 0:
    x_points = [x*width/graph_w for x in range(0, graph_w + 1)]
elif upper_x == 0:
    x_points = [x*width/graph_w for x in range(-graph_w, 1)]
else:
    ratio_x = upper_x/lower_x
    x_points = [x*width/graph_w for x in
                range(math.floor(graph_w/(ratio_x - 1)),
                        math.floor(graph_w*ratio_x/(ratio_x - 1)) + 1)]
upper_x = x_points[-1]

for x in range(4):
    print(f"testing rebasing: {x}")

# Creates a similar list for the y axis
height = upper_y - lower_y
if lower_y == 0:
    y_points = [y*height/graph_h for y in range(0, graph_h + 1)][::-1]
elif upper_y == 0:
    x_points = [x*height/graph_h for x in range(-graph_h, 1)][::-1]
else:
    ratio_y = upper_y/lower_y
    y_points = [y*height/graph_h for y in
                range(math.floor(graph_h/(ratio_y - 1)),
                        math.floor(graph_h*ratio_y/(ratio_y - 1)) + 1)][::-1]

print()
print()
print()

while(True):
    print("input function, using x as the variable: ")
    print("available operations: +, -, *, **, /, log(), sin(), sinh(), cos(), cosh(), tan(), tanh()")
    func = input()
    '''
    Adds "math." before every available
    operation from that library
    because doing "from math import *"
    is illegal and evil
    '''
    for op in ["sin(", "sinh(", "cos(", "cosh(", "tan(", "tanh(", "log("]:
        indexes = find_all(func, op, 0)
        offset = 0
        for index in indexes:
            func = func[:index + offset] + "math." + func[index + offset:]
            offset += 5 
    
    # Loops over a grid created from the two lists of x and y values.
    ''' 
    Its getting kinda tough to find ideas for these
    definitely kinda tough.
    '''
    for (x, y) in [(x, y) for y in y_points for x in x_points ]:
        try:
            # Both float and eval are used to catch complex numbers.
            result = float(eval(func))
        except (NameError, SyntaxError):
            print("invalid function input\n")
            break
        except (ValueError, TypeError, ZeroDivisionError):
            if y == 0:
                print("-", end='')
            elif x == 0:
                print("|", end='')
            else:
                print(" ", end='')
            if x == upper_x:
                print()
            continue
        
        '''
        Checks if the point on the grid is close enought to the
        actual function. If it is, it is printed.
        c changes how close the point needs to be,
        c = 0.5 is from trial and error.
        The axes are printed when x = 0 or y = 0
        '''
        c = 0.5
        if abs(y - eval(func)) <= c*(height/graph_h):
            print("x", end='')
        elif y == 0:
            print("-", end='')
        elif x == 0:
            print("|", end='')
        else:
            print(" ", end='')
        if x == upper_x:
            print()

