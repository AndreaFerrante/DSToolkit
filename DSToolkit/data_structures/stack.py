
class Stack(object):

    '''
    Queues are lists in which data is extracted in a Last In Last Out (LIFO)
    '''

    def __init__(self):
        super().__init__()
        self.stack = list()

    def insert(self, data):
        self.stack.append(data)

    def retrieve(self):
        return self.stack.pop()

    def print_elements(self):
        for el in self.stack:
            print(el)


# Driver code...
stack = Stack()
stack.insert(1)
stack.insert(12)
stack.insert(123)

stack.print_elements()

stack.retrieve()
stack.print_elements()