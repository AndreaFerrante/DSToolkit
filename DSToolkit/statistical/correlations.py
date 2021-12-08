from .statistical_distributions import *
import numpy as np
import random


class Correlations(object):

	def __init__(self):
		super().__init__()


	def PearsonCorrelation(self, x:list, y:list):

		'''
		This correlation index is a linear correlation index. It goes from -1 till 1. This coefficient is ideal 
		when the two variables are linearly related.
		A correlation equal to -1 stands for perfect inverse correlation. A correlation index equal to 1 stands for
		a perfect positive correlation. Basically, Pearson correlation index is the ratio between covariance between 
		X and Y variables and multiplication between their variances.

		param x: first list to analyze to see how much correlation is in place against y variable
		param y: second list to analyze to see how much correlation is in place against x variable
		'''

		pass

	def SpearmanCorrelation(self, x:list, y:list):

		'''
		'''

		pass



