a = input()
word = ""
char = ""
for i in a:
    if i == ' ':
        if char != "":
            word += char
        char = ""
    else:
        char = i
if char != "":
    word += char
print(word)
