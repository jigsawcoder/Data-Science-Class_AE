# This is the solution of the RAINBOW ARRAY problem in codechef
# PYTHON 3.6

T = int(input())
N = int(input())
A = []
for i in range(N):
    x = int(input())
    A.append(x)

if A != A[::-1]:
    print("NO")
else:
    print("YES")


    
