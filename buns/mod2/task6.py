name = input()
res = ''
while 1:
    if len(name) > 0:
        sym = name[0]
        if sym!= '.':
            res += sym
            name = name[1::]
        else:
            print(res)
            name = name[1::]
            res = ''
    else:
        print(res)
        break
