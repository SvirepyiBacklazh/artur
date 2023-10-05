a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = int(input("Введите третее число"))

sum = a+b+c
res = sum - min(a, b, c) - max(a, b, c)
print(res)
