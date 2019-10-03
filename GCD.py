#Using python3.
def gcd(a,b):
    if b == 0:
        return a
    else:
        a_remainder = a % b

    return gcd(b,a_remainder)

a , b = map(int,input().strip().split())
print(gcd(a,b))