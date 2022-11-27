#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#6782 -> 23
#0,56 -> 11

n = int(input('add numbers summ:= '))
suma = 0

while n > 0:
    digit = n % 10
    suma = suma + digit
    n = n // 10
 
print("Сумма:", suma)