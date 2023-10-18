word = input()

def can_create(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    odd_count = 0
    for count in letter_count.values():
        if count % 2 != 0:
            odd_count += 1

    return odd_count <= 1

def build(word):
    if not can_create(word):
        return "Нельзя построить палиндром"

    letter_count = {}
    half = ""
    odd_char = ""
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for letter, count in letter_count.items():
        if count % 2 == 0:
            half += letter * (count // 2)
        else:
            odd_char = letter

    return half + odd_char + half[::-1]

print(build(word))
