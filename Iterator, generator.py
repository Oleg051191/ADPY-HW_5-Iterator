nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:
    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.cursor = 0
        self.cursor_list = -1
        return self

    def __next__(self):
        self.cursor_list += 1
        if len(self.my_list[self.cursor]) == self.cursor_list:
        	self.cursor += 1
        	self.cursor_list = 0
        if self.cursor == len(self.my_list):
            raise StopIteration
        return self.my_list[self.cursor][self.cursor_list]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(my_list):
    for element in my_list:
        for el in element:
            yield el

nested_list = [
	[[[['a', 'b', 'c']]]],
	['d', 'e', 'f'],
	[[1, 2, None]],
	[45, 642, 22, False],
	[1]
]

def flat_generator(my_list):
	for element in my_list:
		if isinstance(element, list):
			for elem in flat_generator(element):
				yield elem
		else:
			yield element

for item in  flat_generator(nested_list):
	print(item)


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    ## Итератор через компрехершн
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)
    ## Генератор через компрехершн
    flat_gen = [item for item in flat_generator(nested_list)]
    print(flat_gen)

    ## Генератор, работающий с любой длинной
    for item in flat_generator(nested_list):
        print(item)
