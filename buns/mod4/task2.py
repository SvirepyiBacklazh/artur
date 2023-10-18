num = int(input())
degree = int(input())

def exponentiation(num, degree):
    if degree == 0:
        return 1
    elif degree % 2 == 0:
        half = exponentiation(num, degree // 2)
        return half * half
    else:
        return num * exponentiation(num, degree - 1)

print(exponentiation(num, degree))
