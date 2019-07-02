t = int(input())
for x in range(t):
    n = int(input())
    line = input()
    c = input()
    l = [int(x) for x in line.split()]
    while len(l) < n:
        result = (l[-c:] + l[:-c])
        print(result)
