
import copy
import threading

NUMBER_OF_THREADS = 8

global task_queue, thread_lock
task_queue = []
thread_lock = threading.Lock()

class Consumer(threading.Thread):
	def __init__(self):
		super().__init__(daemon=True)

		self.size = 0
		self.value = 0
		self.times = 0


	def matrix_mul(self, first: list[int], second: list[int]) -> list[int]:
		res = [[0]*self.size for i in range(self.size)]

		for i in range(self.size):
			for j in range(self.size):
				for k in range(self.size):
					res[i][j] += first[i][k] * second[k][j]

		return res


	def run(self) -> None:
		global task_queue, thread_lock

		while True:
			with thread_lock:
				if not len(task_queue):
					return

				self.size, self.value, self.times = task_queue.pop(0)

			matrix = [[self.value ** (i + j) for j in range(self.size)] for i in range(self.size)]
			cache = copy.deepcopy(matrix)
			for i in range(self.times):
				matrix = self.matrix_mul(matrix, cache)

			print(sum([sum(i) for i in matrix]))


for i in range(40, 60):
	task_queue.append((i, 2, 25))

threads = [Consumer() for i in range(NUMBER_OF_THREADS)]

for tr in threads:
	tr.start()

for tr in threads:
	if tr.is_alive():
		tr.join()

# 11.3 seconds on python3.12.3 with gil
# 2.45 seconds on python3.13.1 no-gil
