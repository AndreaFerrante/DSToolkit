import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def insertionSort(arr):
	n = len(arr)

	for i in range(1, n):

		k = arr[i]
		j = i - 1

		while j >= 0 and arr[j] > k:
			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = k

	return arr


def bubbleSort(arr):
	n = len(arr)

	for i in range(n):
		for j in range(n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	return arr


def binarySearch(arr, el):
	arr = bubbleSort(arr)
	l = 0
	r = len(arr) - 1

	while l <= r:

		m = (l + r) // 2

		if el == arr[m]:
			return True
		elif el < arr[m]:
			r = m - 1
		else:
			l = m + 1

	return False


def recurring_delimiter(str_input):
	new_str = ''
	for i in str_input:
		if i not in new_str:
			new_str += i

	return new_str


def fibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return (fibo(n - 1) + fibo(n - 2))


for i in range(10):
	print(fibo(i))


def list_reverse(arr):
	n = len(arr)
	for i in range(n):
		print(arr[n - i - 1])


def palindrome(input_str):

	n = len(input_str)
	o = n / 2 if n % 2 == 0 else n // 2
	i = 0

	while o > 0:
		if input_str[i] == input_str[n - i - 1]:
			i += 1
			o -= 1
		else:
			return False

	return True


def isPalindrome(input_str):

	p = ''.join(reversed(input_str))

	if input_str == p:
		return True

	return False


def setDuplicates(arr):
	return set([x for x in arr if arr.count(x) > 1])


def gaussian(x, mu=0, sigma=1):
	el_1 = (1 / ((2 * np.pi) ** 0.5 * sigma))
	el_2 = np.exp(-(x - mu) ** 2 / (2 * sigma))

	return el_1 * el_2


def rolling_mean(arr, step=10):
	def get_mean(elements):

		n = len(elements)
		s = 0
		for i in range(n):
			s += elements[i]

		return s / n

	roll_mean = []
	arr_length = len(arr)

	for i, el in enumerate(range(step, arr_length)):
		roll_mean.append(get_mean(arr[i:step + i]))

	return roll_mean


def split(input_str):
	len_str = len(input_str) - 1
	rev_str = ''

	for i in range(0, len_str + 1):
		rev_str += input_str[len_str - i]

	return rev_str


print(split('nice interview'))


def online_generator(max):
	number = 1
	while number < max:
		number += 1
		yield number


def medianFinder(arr):
	def bubbleSort(arr):

		n = len(arr)
		for i in range(n):
			for j in range(n - i - 1):
				if arr[j] > arr[j + 1]:
					arr[j], arr[j + 1] = arr[j + 1], arr[j]

		return arr

	arr = bubbleSort(arr)
	n = len(arr)
	m = (n - 1) // 2

	return arr[m]


arr = [3, 7, 6, 5, 9, 8, 1]
print('Unsorted array is ', arr)
print('Sorted array is ', insertionSort(arr))
print(binarySearch(arr, 7))


#                1
#              /   \
#             2     3
#            / \   /
#           4   5 6



# Binary Tree...
# Binary Tree...
class BinaryTree:

	def __init__(self, data):

		self.data = data
		self.right = None
		self.left = None

	def insert(self, data):

		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = BinaryTree(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = BinaryTree(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data)
		if self.right:
			self.right.PrintTree()

	# Left -> Root -> Right
	def InOrderTraversal(self, root):
		res = []
		if root:
			res = self.InOrderTraversal(root.left)
			res.append(root.data)
			res = res + self.InOrderTraversal(root.right)
		return res

	# Root -> Left -> Right
	def PreOrderTraversal(self, root):
		res = []
		if root:
			res.append( root.data )
			res = res + self.PreOrderTraversal(root.left)
			res = res + self.PreOrderTraversal(root.right)
		return res

	# Postorder traversal
	# Left -> Right -> Root
	def PostOrderTraversal(self, root):
		res = []
		if root:
			res = self.PostOrderTraversal(root.left)
			res = res + self.PostOrderTraversal(root.right)
			res.append(root.data)
		return res

	def InvertTree(self, root):
		self.solve(root)
		return root

	def solve(self, root):
		if not root:
			return
		root.left, root.right = root.right, root.left
		self.solve(root.left)
		self.solve(root.right)




bt = BinaryTree(10)
bt.insert(5)
bt.insert(7)
bt.insert(11)
bt.insert(15)
bt.PrintTree()


print(bt.InOrderTraversal(bt))
print(bt.PreOrderTraversal(bt))
print(bt.PostOrderTraversal(bt))


new_bt = bt.InvertTree(bt)
new_bt.PrintTree()




def solution(A):
    # write your code in Python 3.6
    _ = len( list(set(sorted( A ))) )
    f = float('inf')

    for i in range(_):
        if i + 1 in A:
            pass
        else:
            if i < f:
                f = i + 1

    if f == float('inf'):
        return _ + 1
    else:
        return f







































