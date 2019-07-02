N = int(input("Enter the number: "))
x = N%10

if 0<= x <= 5:
    N = N - x
    print(N)
elif 5< x <9:
    N = N + (10-x)
    print(N)

