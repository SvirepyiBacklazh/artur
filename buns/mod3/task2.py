a = int(input())
rez = (bin(a)[2:], oct(a)[2:], hex(a)[2:]) if a>0 else "Неверный ввод"
print(rez)
