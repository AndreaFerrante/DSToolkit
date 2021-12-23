import numpy as np


#########################################################################################
# This is a class that collects data science "distances methods".
#
# Distances measure similarities between features (both numeric and categorical).
#
# Distances are used in a lot of fields: in Machine Learning inside methods (such as the 
# KNN or the cosine similarity used inside the colloborative filtering tecnique).
#########################################################################################


class Distances(object):

	def __init__(self):
		super().__init__()


	def Euclidean(self, x:list, y:list):

		'''
		Euclidean distance measures distance between points in a linear space. When the space we
		are considering is high dimensional, it suffers from the curse of dimensionality.

		param x: first point in form of [float, float]
		param y: second point in form of [float, float]
		'''

		pass


	def Manhattan(self, x:list, y:list):

		'''
		Manhattan distance refers to the distance between two vectors if they could only move 
		by following right angles. It takes its name from New York Manhattan hood where streets 
		are forming almost always squre root angles against each other.

		param x: first point in form of [float, float]
		param y: second point in form of [float, float]
		'''

		pass


	def Minkowski(self, x:list, y:list):

		'''
		Minkowski distance refers to the distance a metric used in Normed vector space 
		(n-dimensional real space), which means that it can be used in a space where distances
		can be represented as a vector that has a length.

		param x: first point in form of [float, float]
		param y: second point in form of [float, float]
		'''

		pass


	def Hamming(self, x, y):

		'''
		Hamming distance (used for categorical features) measures the distance in terms of different
		values between two vectors. It is tipically used to measure the difference between two strings.

		param x: first object (i.e. "Andrea")
		param y: second point object (i.e. "Annrea")
		'''

		pass


	def CosineSimilarity(self, x:list, y:list):

		'''
		Cosine similarity measure the distance between two vectors getting the cosine among them.
		If the cosine is close two one, these two vectors are equal. If the cosine is almost equal
		to minus one, these two vectors are dissimilar.
		in order to be compared the vector must have same length.

		param x: is it the first vector in form [1,2,4,5]
		param y: is it the first vector in form [1,2,4,7]
		'''

		pass








