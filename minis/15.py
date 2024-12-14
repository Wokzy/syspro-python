
import copy
import threading


class Consumer(threading.Thread):
	def __init__(self, size: int, value: int, times: int):
		super().__init__(daemon=True)

		self.size = size
		self.value = value
		self.times = times

		self.result = None


	def matrix_mul(self, first: list[int], second: list[int]) -> list[int]:
		res = [[0]*self.size for i in range(self.size)]

		for i in range(self.size):
			for j in range(self.size):
				for k in range(self.size):
					res[i][j] += first[i][k] * second[k][j]

		return res


	def run(self) -> None:

		matrix = [[self.value ** (i + j) for j in range(self.size)] for i in range(self.size)]
		cache = copy.deepcopy(matrix)
		for i in range(self.times):
			matrix = self.matrix_mul(matrix, cache)

		self.result = sum([sum(i) for i in matrix])


task_queue = []
for i in range(40, 60):
	task_queue.append(Consumer(size=i, value=2, times=25))
	task_queue[-1].start()

for task in task_queue:
	if task.is_alive():
		task.join()

	print(task.result)

# 11.8 seconds on python3.12.3 with gil
# 2.6 seconds on python3.13.1 no-gil
