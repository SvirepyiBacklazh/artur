side = int(input())
for first in range(1, side+1):
    for second in range(1, side+1):
        if side != second:
            print(second, end = ", ")
        else:
            print(second)
            
print()

for first in range(1, side+1):
    for second in range(1, side+1):
        if side != second:
            print(first, end = ", ")
        else:
            print(first)
