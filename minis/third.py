import pytest

read_matrix = lambda string: [list(map(float, line.strip().split(' '))) for line in string.split(' | ')]


@pytest.mark.parametrize("string, res", [("1 2 | 3 4", [[1.0, 2.0], [3.0, 4.0]]),
										 ("1 2 3 | 3.141592 2.718281828459 10.1", [[1.0, 2.0, 3.0], [3.141592, 2.718281828459, 10.1]]),
										 ("1 | 1 | 1 | 1 | 1 | 1", [[1], [1], [1], [1], [1], [1], ])])
def test(string, res):
	assert read_matrix(string) == res

