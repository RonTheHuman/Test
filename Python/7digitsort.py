print("enter 7 numbers")
out = 0
zeros = 0
# The function gets 7 inputs, after each input checking whether
#   it is valid. If the input is 0, the zeros counter is incremented,
#   in any other case the number is inserted to the final output, such that
#   digits in the output are in increasing order
for i in range(7):
    x = input()
    while len(x) != 1 or not x.isdigit(): # validity check: numbers from 0 to 9
        print("incorrect input")
        x = input()
    x = int(x)
    
    if x == 0:
        zeros += 1
    # x is inserted into out by first consecutively deviding a temp 
    #   variable by 10 to find the insert position, then adding x as the
    #   last digit of the temp variable, and finally adding temp_out 
    #   in front of the digits of out, without overlap.
    temp_out = out
    pos = 0
    while x < temp_out % 10:
        temp_out = int(temp_out / 10)
        pos += 1
    temp_out = temp_out * 10 + x
    out = out % pow(10, pos)
    temp_out *= pow(10, pos)
    out += temp_out
    

for i in range(zeros):
    # zero can be always printed first since it will 
    #   always be the smallest input 
    print("0", end="") 
print(out)
