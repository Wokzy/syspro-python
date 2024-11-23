
def cycle(iterable):

	while True:
		for i in iterable:
			yield i


class chain:
	def __init__(self, *args):
		self.args = args

	def __iter__(self):
		self.current = 0
		self.iterator = self.args[0].__iter__()
		return self

	def __next__(self):
		try:
			return self.iterator.__next__()
		except StopIteration:
			self.current += 1
			if self.current >= len(self.args):
				raise StopIteration

			self.iterator = self.args[self.current].__iter__()
			return self.__next__()



# def chain(*args):

# 	for current in args:
# 		for i in current:
# 			yield i



def test():
	br = 100
	for i in cycle(chain([1, 2, 3], 'ab', 'qqqq')):
		if br <= 0:
			break
		print(i)
		br -= 1

	print(list(chain([1, 2, 3], ['a', 'b'])))

if __name__ == '__main__':
	test()
