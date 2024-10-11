import pytest


def reverse_dict(hashtable: dict) -> dict:
	""" Has O(n) time complexity and O(n) memory complexity """
	result = {}

	for key, value in hashtable.items():
		if value in result.keys():
			result[value].append(key)
		else:
			result[value] = [key]

	for key in result.keys():
		if len(result[key]) == 1:
			result[key] = result[key][0]
		else:
			result[key] = tuple(result[key])

	return result


@pytest.mark.parametrize("i, o", [({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}, {97832: ("Ivanov", "Kuznecov"), 55521: "Petrov"})])
def test(i, o):
	assert reverse_dict(i) == o

