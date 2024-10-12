import pytest


my_zipper = lambda a, b: [(a[i], b[i]) for i in range(min(len(a), len(b)))]

@pytest.mark.parametrize("a, b, res", [[[1, 2, 3], ['a', 'b'], [(1, 'a'), (2, 'b')]],
									   ([5, 5], [(1, 2), (10.321, False)], [(5, (1, 2)), (5, (10.321, False))]),
									   ([1, 2, 3, 4], [], [])])
def test(a, b, res):
	assert my_zipper(a, b) == res
