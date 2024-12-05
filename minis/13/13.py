
import copy
import numpy
import foreign


def test_1():
	power = 10
	matrix = [[1.0, 1.0], [2.0, -5.432]]

	res = numpy.array(foreign.foreign_matrix_power(matrix, power))
	cache = numpy.array(copy.deepcopy(matrix))
	matrix = numpy.array(matrix)

	for i in range(power):
		matrix @= cache

	assert matrix.all() == res.all()


if __name__ == '__main__':
	test_1()
