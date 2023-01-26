import random

while True:
    
    colattempt = int(input("Сколько попыток будет? "))

    print('Выбери диапазон (от a до b): ')
    a = int(input("a = "))
    b = int(input("b = "))

    number = random.randint(a, b)
    i = 0
    
    while i < colattempt:
        attempt = int(input("Ваше предположение: "))
    
        if abs(attempt - number) <= 5 and abs(attempt - number) != 0:
            print('близко') 
        if abs(attempt - number) > 5 and abs(attempt - number) <= 10:
            print('не совсем')
        if abs(attempt - number) > 10:
            print('постарайся ещё')
        if attempt == number:
            print('молодец, правильный ответ')
            break
            
        i += 1
        
        if i == colattempt:
            print('Game Over!  Правильный ответ был ', number)
            break
