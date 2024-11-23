

def singleton(cls):
	cls.instance = None
	cls.init = False
	initial_new = cls.__new__
	initial_init = cls.__init__

	def new_init(cls, *args, **kwargs):
		if cls.init:
			return

		initial_init(cls, *args, **kwargs)
		cls.init = True

	def __new__(cls, *args, **kwargs):
		if cls.instance is None:
			cls.instance = initial_new(cls, *args, **kwargs)

		return cls.instance

	cls.__new__ = __new__
	cls.__init__ = new_init
	return cls



@singleton
class SingletonTest:
	def __init__(self, some_info:str = 'popopo'):
		print('312')
		self.some_info = some_info


def test():
	a = SingletonTest()
	b = SingletonTest()

	assert id(a) == id(b)

if __name__ == '__main__':
	test()
