

def singleton(cls):
	cls.instance = None
	initial_new = cls.__new__

	def __new__(cls, *args, **kwargs):
		if cls.instance is None:
			cls.instance = initial_new(cls, *args, **kwargs)

		return cls.instance

	cls.__new__ = __new__
	return cls



@singleton
class SingletonTest:
	def __init__(self, some_info:str = 'popopo'):
		self.some_info = some_info


def test():
	a = SingletonTest()
	b = SingletonTest()

	assert id(a) == id(b)

if __name__ == '__main__':
	test()
