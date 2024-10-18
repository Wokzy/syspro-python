

def specialize(function, *args, **kwargs):

	def _res(*new_args, **new_kwargs):
		for k in new_kwargs.keys():
			if k in kwargs.keys():
				raise TypeError(f"function specialized on {function.__name__} doesn't take positional argument {k}")

		function(*args, *new_args, **kwargs, **new_kwargs)

	return _res


def foo_test_1(k):
	print(k)

def foo_test_2(a, b):
	print(a, b)


def test():
	try:
		specialize(foo_test_1, k=3)(k=4) # TypeError
	except TypeError as e:
		print(f"TypeError: {e}")

	specialize(foo_test_2, 1, 2)()   # -> 1, 2
	specialize(foo_test_2, b=2)(10)  # -> 10, 2


if __name__ == "__main__":
	test()
