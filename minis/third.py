import pytest

read_matrix = lambda string: [list(map(float, line.strip().split(' '))) for line in string.split(' | ')]


@pytest.mark.parametrize("string, res", [("1 2 | 3 4", [[1.0, 2.0], [3.0, 4.0]])])
def test(string, res):
	assert read_matrix(string) == res

