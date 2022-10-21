
class Queue(object):

	'''
	Queues are lists in which data is extracted in a First In First Out (FIFO)
	'''

	def __init__(self):
		super().__init__()
		self.queue = list()

	def insert(self, data):
		self.queue.append(data)

	def retrieve(self):
		return self.queue.pop(0)

	def print_elements(self):
		for el in self.queue:
			print(el)


# Driver code...
q = Queue()
q.insert(10)
q.insert(111)
q.insert('element')

print('elements with no pop are')
q.print_elements()

print('elements after pop are')
q.retrieve()
q.print_elements()