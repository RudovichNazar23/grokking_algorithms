
def gcd(a: int, b: int):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
