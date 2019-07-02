def euclid_gcd(a, b):
    dividend = a if a>=b else b
    divisor = a if a<=b else b
    while(divisor != 0):
        remainder= dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend

a = int(input("Enter a num: "))
b = int(input("Enter a nume: "))

gcd = euclid_gcd(a,b)

print("GDC of a and b is ", gcd)
