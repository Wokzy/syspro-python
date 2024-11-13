
import heapq


class Unit:
	def __init__(self, name, value, counter:int):
		self.name = name
		self.value = value
		self.counter = counter

	def __lt__(self, second):
		self.counter < second.counter

	def __gt__(self, second):
		self.counter > second.counter

	def __le__(self, second):
		self.counter <= second.counter

	def __ge__(self, second):
		self.counter >= second.counter


class LRUCache:

	def __init__(self, capacity=16):

		self.capacity = capacity
		self.counter = 0
		self.mapping = {}
		self.heap = []


	def get(self, name):
		if name in self.mapping:
			self.mapping[name].counter = self.counter
			self.counter += 1
			if len(self.heap) > 1:
				heapq._siftdown(self.heap, 0, len(self.heap) - 1)
			return self.mapping[name].value
		else:
			return


	def put(self, name, value):
		if name in self.mapping:
			return

		if len(self.mapping) == self.capacity:
			obj = heapq.heappop(self.heap)
			del self.mapping[obj.name]

		self.mapping[name] = Unit(name, value, self.counter)
		self.counter += 1
		heapq.heappush(self.heap, self.mapping[name])


def fibonacci(n:int, cache:LRUCache) -> int:
	if n <= 2:
		return 1

	a = cache.get(n)
	if a is not None:
		return a

	res = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
	cache.put(n, res)
	return res


def test():
	print(fibonacci(200, LRUCache(32)))

if __name__ == '__main__':
	test()

