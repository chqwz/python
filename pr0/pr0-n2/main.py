import random

print("Введите диапазон (от a до b): ")
a = int(input("a = "))
b = int(input("b = "))

number = int(input("Загадайте число: "))

attempt = random.randint(a, b)
tries = 1

if number == attempt:
    print('Я угадал с первой попытки)')
else:
    while attempt != number:
        if number > attempt:
            print("Думаю, это число ", attempt)
            a = attempt
            attempt = random.randint(a, b)
            tries += 1
            
        elif number < attempt:
            print("Думаю это число  ", attempt)
            b = attempt
            attempt = random.randint(a, b)
            tries += 1
            
    print (number)
    print ('Я угадал с', tries, 'попытки')