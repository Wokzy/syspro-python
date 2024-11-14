
from functools import wraps

def специализировать(функция, *арги, **кварги):

	def _результат(*новые_арги, **новые_кварги):
		return функция(*арги, *новые_арги, **кварги, **новые_кварги)

	return _результат


def deprecated(функция = None, *, since:str = '', will_be_removed:str = ''):

	if функция is None:
		return специализировать(deprecated, since=since, will_be_removed=will_be_removed)

	@wraps(функция)
	def inner(*args, **kwargs):
		depr_string = f'Warning: function {функция.__name__} is deprecated'

		if since:
			depr_string += f' since version {since}'
		depr_string += '. It will be removed in '

		if will_be_removed:
			depr_string += f'version {will_be_removed}.'
		else:
			depr_string += 'future versions.'

		print(depr_string)

		функция(*args, **kwargs)

	return inner


@deprecated
def foo():
	print('foo')

@deprecated(since='3.13.0rc1')
def boo():
	print('boo')

@deprecated(since='3.13.0rc1', will_be_removed='3.13.1')
def sdadfgdsfg():
	print('sdadfgdsfg')

@deprecated(will_be_removed='3.12.8')
def menya_zovyt_yegor():
	print('menya_zovyt_yegor')


def test():
	foo()
	boo()
	sdadfgdsfg()
	menya_zovyt_yegor()


if __name__ == "__main__":
	test()
