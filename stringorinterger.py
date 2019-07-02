# THIS CODE RETURN INTERGER IF THE GIVEN INPUT IS INTEGER AND STRING OF ANYTHING ELSE
# PYTHON 3.6

# T is the number of test cases

T = int(input("Enter the number of test cases: "))

for i in range(T):

    X = input("Enter your input here: \n")
    for x in X:
        if x.isdigit() == True :
            a = 1
        else:
            a = 0
    
if a == 1:
    print("Given input is interger. \n")
else:
    print("Given input is string. \n")
