import numpy as np


############################################################################################
# This is a class that collects statistical indexes such as mean, variance and permutations.
############################################################################################


class StatisticalIndexes(object):


	def __init__(self):
		super().__init__()


	def Factorial(self, n:int):

		'''
		...same of from math import factorial !
		'''

		res = 1
		for i in range(2, n + 1):
			res *= i

		return res


	def Power(self, base:float, exp:int):

		'''
		...it would be easier to use the ** Python operator, but it would be less funny !
		'''

		if base == 0:
			return 0
		elif base == 1:
			return 1
		else:
			res = base
			for i in range(2, exp + 1):
				res *= base
			return res


	def Mean(self, x:list=None):

		return sum(x) / len(x)


	def SampleVariance(self, x:list=None):

		s_mean = self.Mean( x )
		num    = sum( [(j - s_mean)**2 for j in x] )
		den    = len(x) - 1

		return num / den


	def Variance(self, x:list=None):

		mean   = self.Mean( x )
		num    = sum( [(j - mean)**2 for j in x] )
		den    = len(x)

		return num / den


	def StandardDeviationSample(self, x:list):

		return self.SampleVariance(x) ** 0.5


	def StandardDeviation(self, x:list):

		return self.Variance(x) ** 0.5


	def Covariance(self, x:list, y:list):

		'''
		Attention: X and Y variables must have same array length.
		'''

		mean_x = self.Mean(x)
		mean_y = self.Mean(y)

		den = len(x) - 1
		num = sum( [ (x[j] - mean_x) * (y[j] - mean_y) for j in range( den + 1 ) ] )

		return num / den








