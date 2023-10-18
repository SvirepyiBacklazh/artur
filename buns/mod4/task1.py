numbers = input()

def check(numbers):
    if all(num == numbers[0] for num in numbers):
        return "Все числа равны"
    elif len(set(numbers)) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"

print(check(numbers))    
