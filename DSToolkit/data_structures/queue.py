
class Queue(object):

	'''
	Queues are lists that insert data using FIFO manner: the first element inserted is the one that is
	extracted first (first in first out). The opposite data structure is the stack (LIFO, last in first out)
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

q.print_elements()
q.retrieve()
q.print_elements()