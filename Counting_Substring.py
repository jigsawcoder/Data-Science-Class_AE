T = int(input())

for x in range(T):
    N = int(input())
    string = 'N'
    U = input()
    string += U
    n = string.count('1')
    j =  ((n*(n+1))/2)
    print(j)
    string = ''
