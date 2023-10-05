code = input()
honest = 0
odd = 0
b = True
while True:
    if len(code)!= 0:
        i = code[0]
        code = code[1::]
        if b:
            odd += int(i)
            b = False
        else:
            honest += int(i)
            b = True
    else:
        break
if (3 * honest + odd) %10 == 0:
    print('yes')
else:
    print('no')
