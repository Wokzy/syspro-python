


def bit_count(number: int) -> int:
	res = 0

	if number > 0:
		while number > 0:
			res += number & 1
			number >>= 1
	elif number < 0:
		res += 1
		number = abs(number)
		q = number

		c = 0
		while q > 0:
			c += 1
			q >>= 1

		number -= 1


		for i in range(c):
			res += (number & 1) ^ 1
			number >>= 1

	return res


print(bit_count(int(input("Enter number -> "))))
