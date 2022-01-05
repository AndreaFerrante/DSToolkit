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


n1      = Node(1)
n2      = Node(2)
n3      = Node(3)

linked_list      = LinkedList()
linked_list.head = n1
n1.next = n2
n2.next = n3

linked_list.PrintList()

