# This is the solution of the problem The Minimum Number Of Moves by CodeChef
# PYTHON 3.6

# N - Number of Workers

N = int(input())
W = []

for i in range(N):
    x = int(input())    # Enter the salary of this worker here.
    W.append(x)

W.sort(reverse=True)

count = 0

for j in range((N-1)):
    for k in 
    
