#Using python3.
def gcd(a,b):
    if b == 0:
        return a
    else:
        a_remainder = a % b

    return gcd(b,a_remainder)

def lcm_naive(a, b):
    lcm = (a*b) // (gcd(a,b))
    return lcm


a , b = map(int,input().strip().split())

print(lcm_naive(a,b))



