
import copy
import time
import numpy
import random

from functools import wraps


def timeit(func):
	@wraps(func)
	def timeit_wrapper(*args, **kwargs):
		start_time = time.perf_counter()
		result = func(*args, **kwargs)
		end_time = time.perf_counter()
		total_time = end_time - start_time
		print(f'Function {func.__name__} Took {total_time:.4f} seconds')
		return result
	return timeit_wrapper



def calc_neighbors(a, i, j, shape):
	n = shape[0]
	m = shape[1]
	return a[(i + n - 1) % n][(j + m - 1) % m] + \
		   a[(i + n - 1) % n][j] + \
		   a[(i + n - 1) % n][(j + m + 1) % m] + \
		   a[i][(j + m + 1) % m] + \
		   a[i][(j + m - 1) % m] + \
		   a[(i + n + 1) % n][(j + m - 1) % m] + \
		   a[(i + n + 1) % n][j] + \
		   a[(i + n + 1) % n][(j + m + 1) % m]


def make_move_basic(a, cache, shape: tuple[int, int]) -> None:
	for i in range(shape[0]):
		for j in range(shape[1]):
			neighbors = calc_neighbors(a, i, j, shape)

			if neighbors <= 1 or neighbors >= 4:
				cache[i][j] = 0
			elif not a[i][j] and neighbors == 3:
				cache[i][j] = 1
			else:
				cache[i][j] = a[i][j]


def make_move_numpy(a, cache, shape: tuple[int, int]) -> None:
	n = shape[0]
	m = shape[1]
	for i in range(shape[0]):
		for j in range(shape[1]):
			neighbors = a[(i + n - 1) % n, (j + m - 1) % m] + \
						a[(i + n - 1) % n, j] + \
						a[(i + n - 1) % n, (j + m + 1) % m] + \
						a[i, (j + m + 1) % m] + \
						a[i, (j + m - 1) % m] + \
						a[(i + n + 1) % n, (j + m - 1) % m] + \
						a[(i + n + 1) % n, j] + \
						a[(i + n + 1) % n, (j + m + 1) % m]
			#calc_neighbors(a, i, j, shape)

			if neighbors <= 1 or neighbors >= 4:
				cache[i, j] = 0
			elif not a[i, j] and neighbors == 3:
				cache[i, j] = 1
			else:
				cache[i, j] = a[i, j]


def make_move_numpy_via_item(a, cache, shape: tuple[int, int]) -> None:
	n = shape[0]
	m = shape[1]
	for i in range(shape[0]):
		for j in range(shape[1]):
			neighbors = a.item((i + n - 1) % n, (j + m - 1) % m) + \
						a.item((i + n - 1) % n, j) + \
						a.item((i + n - 1) % n, (j + m + 1) % m) + \
						a.item(i, (j + m + 1) % m) + \
						a.item(i, (j + m - 1) % m) + \
						a.item((i + n + 1) % n, (j + m - 1) % m) + \
						a.item((i + n + 1) % n, j) + \
						a.item((i + n + 1) % n, (j + m + 1) % m)
			#calc_neighbors(a, i, j, shape)

			if neighbors <= 1 or neighbors >= 4:
				cache[i, j] = 0
			elif not a[i, j] and neighbors == 3:
				cache[i, j] = 1
			else:
				cache[i, j] = a.item(i, j)



shape = (1024, 1024)
data = [[random.randint(0, 1) for i in range(shape[1])] for j in range(shape[0])]
empty = [[0]*shape[1] for i in range(shape[0])]

@timeit
def main(a, cache, make_move_f):
	global shape, data, empty

	for i in range(2):
		if (i & 1):
			make_move_f(cache, a, shape)
		else:
			make_move_f(a, cache, shape)


def test_numpy():
	global data, empty
	print('Testing numpy (numpy indexing [i, j]): ')
	array = numpy.array(data, dtype='uint8')
	cache = numpy.array(empty, dtype='uint8')

	main(array, cache, make_move_numpy)

	print('Testing numpy (native indexing): ')
	array = numpy.array(data, dtype='uint8')
	cache = numpy.array(empty, dtype='uint8')
	main(array, cache, make_move_basic)

	print('Testing numpy (numpy.darray.item indexing): ')
	array = numpy.array(data, dtype='uint8')
	cache = numpy.array(empty, dtype='uint8')
	main(array, cache, make_move_basic)

def test_simple():
	global data, empty
	print('Testing simple: ')
	array = copy.deepcopy(data)
	cache = copy.deepcopy(empty)

	main(array, cache, make_move_basic)


if __name__ == '__main__':
	test_numpy()
	test_simple()
