num = input()
val = "0123456789+"
res = ""
for i in num:
    if i in val:
        res += i
print(res)
