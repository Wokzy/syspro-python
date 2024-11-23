
def cycle(iterable):
	it = iterable.__iter__()

	while True:
		try:
			yield it.__next__()
		except StopIteration:
			it = iterable.__iter__()


def chain(*args):

	for current in cycle(args):
		it = current.__iter__()
		while True:
			try:
				yield it.__next__()
			except StopIteration:
				break


def test():
	br = 100
	for i in cycle([1, 2, 3]):
		if br <= 0:
			break
		print(i)
		br -= 1

	br = 100
	for i in chain([1, 2, 3], ['a', 'b']):
		if br <= 0:
			break
		print(i)
		br -= 1

if __name__ == '__main__':
	test()
