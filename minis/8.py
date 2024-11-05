

def format_table(rows:list[str], columns:list[str], data:list[...]) -> str:

	for i in range(len(rows)):
		data[i].insert(0, rows[i])

	columns.insert(0, 'Benchmark')

	sizes = [len(columns[i]) + 2 for i in range(len(columns))]
	sm = 0
	for i in range(len(columns)):
		for j in range(len(data)):
			data[j][i] = str(data[j][i])
			if len(data[j][i]) + 2 > sizes[i]:
				sizes[i] = len(data[j][i]) + 2

		sm += sizes[i]

	res = '|'

	for i in range(len(columns)):
		res += f' {columns[i]:<{sizes[i] - 1}}|'

	res += '\n|' + '-'*(sm + len(columns) - 1) + '|'
	for i in range(len(data)):
		res += '\n|'
		for j in range(len(data[i])):
			res += f' {data[i][j]:<{sizes[j] - 1}}|'

	return res



if __name__ == '__main__':
	print(format_table(
				 ["best case", "worst case"],
				 ["quick sort", "merge sort", "bubble sort", "count sort"],
				 [[1.23, 1.56, 2.0, 0.2], [3.3, 2.9, 3.9, 0.2]]))

	print()

	print(format_table(
				 ["Дорогой", "обидела"],
				 ["Личный", "Дневник", "Егора"],
				 [["Дневник,", "сегодя", "меня"], ["преподаватель", "по ДМТА", "=("]]))
