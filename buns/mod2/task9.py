chars = input()
vowel = "аеёиоуыэюя"
cons = "бвгджзйклмнпрстфхцчшщ"
count_vowel = 0
count_cons = 0
for i in chars:
    if i in vowel:
        count_vowel += 1
    elif i in cons:
        count_cons += 1
print(count_vowel, count_cons)
