

def coroutine(generator):

	def __inner(*args, **kwargs):
		gen = generator(*args, **kwargs)
		next(gen)
		return gen

	return __inner

@coroutine
def storage():
	values = set()
	was_there = False

	while True:
		val = yield was_there
		was_there = val in values
		if not was_there:
			values.add(val)


st = storage()
print(st.send(42))
print(st.send(42))
