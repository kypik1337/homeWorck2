#создает список из рандомных четырех значных чисел

from random import randint
numb = []
for i in range (10):
    numb.append(randint(100, 1000))  
print(numb)  