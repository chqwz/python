import random

num = random.randint(10000, 99999)
print("Число: ", num)
x = [int(a) for a in str(num)]  #перевожу число в список
print(x)

m = 0

for i in range(len(x)):  #ищу максимальное число
    if x[i] > m:
        m = x[i]

for i in range(len(x)):  #дублирую максимальный элемент
    if x[i] == m:
        x.insert(x.index(x[i]), m)  
        break

print("new : ", x)

result = int(''.join(map(str, x))) #перевожу список в единое число
print("Результат: ", result)

