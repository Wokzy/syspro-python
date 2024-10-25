


def flatten(arr: list[...], depth=-1) -> list:
	"""
	>>> flatten([1, 2, [2, [3, 4, 5]]])
	[1, 2, 2, 3, 4, 5]
	>>> flatten([1, 2, [2, [3, 4, 5]]], depth=1)
	[1, 2, 2, [3, 4, 5]]
	>>> flatten([1, 2, [4, 5], [6, [7]], 8])
	[1, 2, 4, 5, 6, 7, 8]
	>>> flatten([1, 2, [4, 5], [6, [7]], 8], depth=1)
	[1, 2, 4, 5, 6, [7], 8]
	"""


	res = []
	for i in range(len(arr)):
		if isinstance(arr[i], list) and depth != 0:
			res.extend(flatten(arr[i], depth=depth-1))
		else:
			res.append(arr[i])

	return res


if __name__ == "__main__":
	import doctest
	doctest.testmod()
