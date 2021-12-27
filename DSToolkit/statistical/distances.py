#########################################################################################
# This is a class that collects data science "distances methods".
#
# Distances measure similarities between features (both numeric and categorical).
#
# Distances are used in a lot of fields: in Machine Learning inside methods (such as the 
# k-Means or the cosine similarity used inside the colloborative filtering tecnique).
#########################################################################################

import numpy as np

class Distances(object):

	def __init__(self):
		super().__init__()


	def Euclidean(self, points_1:list, points_2:list):

		'''
		Euclidean distance measures distance between points in a linear space. When the space we
		are considering is high dimensional, it suffers from the curse of dimensionality.

		param points_1: first point in form of [float, float]
		param points_2: second point in form of [float, float]
		'''

		return ( sum( (x - y) ** 2 for x, y in zip(points_1, points_2) ) ) ** 0.5


	def Manhattan(self, points_1:list, points_2:list):

		'''
		Manhattan distance refers to the distance between two vectors if they could only move 
		by following right angles. It takes its name from New York Manhattan hood where streets 
		are forming almost always squre root angles against each other.

		points_1: first point in form of list
		points_2: second point in form of list
		'''

		return sum( abs(x - y) for x, y in zip(points_1, points_2) )


	def Minkowski(self, p_order:float, x:list, y:list):

		'''
		Minkowski distance refers to the distance a metric used in Normed vector space 
		(n-dimensional real space), which means that it can be used in a space where distances
		can be represented as a vector that has a length.
		When p_order is equal to 1, this distance is the Mahnattan one.
		When p_order is equal to 2, this distance is the Euclidean one.

		param x: first point in form of [float, float]
		param y: second point in form of [float, float]
		'''

		assert len(x) == len(y)

		return ( sum( [abs(i - j) ** p_order for i, j in zip(x, y)] ) ) ** (1 / p_order)


	def Hamming(self, x:str, y:str):

		'''
		Hamming distance (used for categorical features such as strings) measures the distance in terms of different
		values between two vectors. It is tipically used to measure the difference between two strings.

		param x: first object (i.e. "Andrea")
		param y: second point object (i.e. "Annrea")
		'''

		assert len(x) == len(y)

		distance = 0
		length   = len(x)

		for i in range(length):
			if x[i] != y[i]:
				distance +=1

		return (length, distance)


	def CosineSimilarity(self, x:list, y:list):

		'''
		Cosine similarity measure the distance between two vectors getting the cosine among them.
		If the cosine is close to one, these two vectors are equal. If the cosine is almost equal
		to minus one, these two vectors are dissimilar.
		in order to be compared the vector must have same length.

		param x: is it the first vector in form [1,2,4,5]
		param y: is it the first vector in form [1,2,4,7]
		'''

		dot    = np.dot( x, y)
		norm_x = ( sum( [ k**2 for k in x ] ) ) ** 0.5
		norm_y = ( sum( [ k**2 for k in y ] ) ) ** 0.5

		return dot / (norm_x * norm_y)


