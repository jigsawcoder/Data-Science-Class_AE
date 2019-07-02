# This code is the solution of Little Elephant and Candies in CodeChef

N = int(input("Enter the number of Elephants."))
C = int(input("Enter the total number of Candies."))

E = [N]

T = int(input("Enter the total number of Test Cases"))

# T defines the number of times the test cases will run.

for y in range(T):
    for x in range(N):
        E.append(x)
        if C >= x:
            C = C - E[x]
        else:
            C = -1

    if C>=0:
        print("Yes")
    else:
        print("No")

    
