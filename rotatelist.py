t = int(input())                #Test Case
for x in range(t):
    n = int(input())            #Array Length
    a = int(input())                 #Rotate Lenght
    line = input()
    l = [int(c) for c in line.split()]
    print(l)
    if n==len(l):
        l1 = l[-a:] + l[:-a]
        print(l1)
    else:
        print("error")
