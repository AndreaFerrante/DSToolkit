import numpy as np
import math

import sys
from pathlib import Path


#############################################
root_path = Path(__file__).parents
sorting_  = str( root_path[1] ) + '/sorting/'

sys.path.append( sorting_ )
from quick_sort import *
#############################################



############################################################################################
# This is a class that collects statistical indexes such as mean, variance and permutations.
############################################################################################


class StatisticalIndexes(object):


	def __init__(self):
		super().__init__()


	def Ranker(self, x:list):

		x_ = quick_sort(x)
		n  = len(x)
		r  = []

		for i in range(n):
			for j in range(n):

				if x[i] == x_[j]:
					r.append(j + 1)
					break

		return r


	def Combination(self, n:int, k:int):

		num = math.factorial(n)
		den = math.factorial(k) * math.factorial(n - k) 

		return num / den


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

		assert len(x) == len(y)

		mean_x = self.Mean(x)
		mean_y = self.Mean(y)

		den = len(x) - 1
		num = sum( [ (x[j] - mean_x) * (y[j] - mean_y) for j in range( den + 1 ) ] )

		return num / den






