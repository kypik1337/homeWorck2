#дайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.


n = int(input('add numbers summ:= '))
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')