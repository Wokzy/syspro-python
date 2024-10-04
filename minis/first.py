import pytest

def bit_count(number: int) -> int:
	res = 0
	negative = False

	if number < 0:
		res += 1
		number = abs(number)
		negative = True

	number -= negative

	while number > 0:
		res += (number & 1) ^ negative
		number >>= 1

	return res


# print(bit_count(int(input("Enter number -> "))))

# 123 -> 0b1111011, -123 -> 1b0000101, -4 -> 1b00
@pytest.mark.parametrize("i, o", [[123, 6], [-123, 3], [10, 2], [-4, 1]])
def test(i, o):
	assert bit_count(i) == o