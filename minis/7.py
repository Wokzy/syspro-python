
def specialize(function, *args, **kwargs):

	def _res(*new_args, **new_kwargs):
		return function(*args, *new_args, **kwargs, **new_kwargs)

	return _res


def deprecated(function = None, *, since:str = '', will_be_removed:str = ''):

	if function is None:
		return specialize(deprecated, since=since, will_be_removed=will_be_removed)

	def inner(*args, **kwargs):
		depr_string = f'Warning: function {function.__name__} is deprecated'
		if since and will_be_removed:
			print(f"{depr_string} since version {since}. It will be removed in version {will_be_removed}")
		elif will_be_removed:
			print(f"{depr_string}. It will be removed in version {will_be_removed}")
		elif since:
			print(f"{depr_string} since version {since}. It will be removed in future versions")
		else:
			print(f"{depr_string}. It will be removed in future versions.")

		function(*args, **kwargs)

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
