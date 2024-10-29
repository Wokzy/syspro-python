
import pytest

def specialize(function, *args, **kwargs):

	def _res(*new_args, **new_kwargs):
		return function(*args, *new_args, **kwargs, **new_kwargs)

	return _res


def foo_test_1(k):
	return k

def foo_test_2(a, b):
	return b, a


def test_exception():
	try:
		specialize(foo_test_1, k=3)(k=3)# TypeError
		assert False, "No exception"
	except Exception as e:
		assert isinstance(e, TypeError)

def test_1():
	assert specialize(foo_test_2, 1, 2)() == (2, 1)

def test_2():
	assert specialize(foo_test_2, b=1)(10) == (1, 10)
