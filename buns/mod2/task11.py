num = input()
f = False
while True:
    for i in range(0, len(num)):
        for k in range(0, len(num)):
            if i!=k:
                if num[i] == num[k] and num[i] != " ":
                    f = True
                    break
    break
print(f)
