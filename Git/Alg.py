# Wrong gcd find 5 mistakes

def gcd(a, b):
    assert a >= 0 and b >= 0

    if a == 0:
        return b

    if b == 0:
        return a

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a



print(gcd(1000000, 64))
# Examples

# gcd(10, 0) => 10
# gcd(123, 3) => 3
# gcd(1000000, 64) => 64
# gcd(0, 0) => 0