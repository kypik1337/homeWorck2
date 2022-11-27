#Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

from random import sample


if __name__ == '__main__':
	nums = range(7)
	l = sample(nums, len(nums))
	print(l)
