class Node:

	def __init__(self, data):

		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):

		self.head = None

	def PrintList(self):

		value = self.head
		
		while value is not None:

			print(value.data)
			value = value.next

	def AddAtBeginning(self, new_data):

		NewHead      = Node(new_data)
		NewHead.next = self.head
		self.head    = NewHead

	def AddAtEnd(self, new_data):

		LastNode = Node(new_data)
		value    = self.head
		
		while value.next:
			value = value.next

		value.next = LastNode



n1      = Node(1)
n2      = Node(2)
n3      = Node(3)

linked_list      = LinkedList()
linked_list.head = n1
n1.next          = n2
n2.next          = n3


linked_list.AddAtBeginning(111)
linked_list.AddAtEnd(222)
linked_list.PrintList()

