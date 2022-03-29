
class Queue(object):

	'''
	Queues are list that insert data using FIFO extraction tecnique: the first element inserted is the one that is 
	'''

	def __init__(self):
		super().__init__()
		self.queue = list()

	def insert(self, data):

		self.queue.append(data)

	def retrieve(self):

		return self.queue.pop(0)

