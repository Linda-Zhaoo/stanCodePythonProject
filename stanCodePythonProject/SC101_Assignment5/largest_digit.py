"""
File: largest_digit.py
Name: Linda Zhao
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: input number
	:return: int, the biggest number of the input
	"""
	largest = 0
	if n < 0:
		n *= -1
	if n < 10:
		return n
	return find_largest_digit_helper(n, largest)


def find_largest_digit_helper(n, largest):
	"""
	:param n: int, number
	:param largest:
	:return: int, the biggest number of the input
	"""
	if n < 10:
		if n > largest:
			largest = n
		return largest
	else:
		a = n % 10
		n = n // 10
		if a > largest:
			largest = a
		return find_largest_digit_helper(n, largest)


if __name__ == '__main__':
	main()
