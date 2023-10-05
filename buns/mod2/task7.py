balanch= input("Введите баланс")
count_one = 0
count_zero = 0
for i in balanch:
    if i == "1":
        count_one +=1
    else:
        count_zero +=1
if count_one == count_zero:
    print("yes")
else:
    print("no")
