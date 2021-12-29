#############################################################
# This is a class that collects statistical distributions.
# This distributions are the essential ones to be remembered.
#############################################################


import numpy as np
import random

from factory import *



class StatisticalDistributions(object):

	def __init__(self):
		super().__init__()


	def Exponential(self, x:float=0, l:float=0, vector:list=None):

		'''
		param x: this is the real number to be processed into an Exponential Distributions
		param l: this is the lambda value of an Exponential Distributions
		param vector: passing this list, these values will be indexes to get corresponding exponential values
		              This value should start from zero and has no upper limit (X belongs to REAL)
		'''

		if vector is None:
			return l * np.exp( -l * x )
		else:
			return [ self.Exponential(x, l, vector=None) for x in vector ]

	def Gaussian(self, x:float=0, mu:float=0, sigma:float=1, vector:list=None):

		'''
		param mu: this is the real mean of our gaussian distribution
		param sigma: this is the variance of our gaussian distribution
		param vector: passing this list, these values will be indexes to get corresponding exponential values
		'''

		if vector is None:
			return (1 / (sigma * (2 * np.pi) ** 0.5 )) * ( np.exp( -((x - mu) / (2 * sigma))**2 ) )
		else:
			return [ self.Gaussian(x=x / 100, mu=mu, sigma=sigma, vector=None) for x in vector ]

	def Poisson(self, x:int=0, l:float=0, vector:list=None):

		'''
		param l: this is the lambda value of a Poisson Distribution
		param vector: passing this list, these values will be indexes to get corresponding exponential values
		              This value should start from zero and has no upper limit (X belongs to REAL)
		'''

		if vector is None:
			return (np.exp(-l) * (l ** x)) / ( self._Factorial( x ) )
		else:
			return [ self.Poisson(x=x, l=l, vector=None) for x in vector ]


	def Binomial(self, n:int, k:int, p:float):

		'''
		param n: number of time the experiment is conducted
		param k: number of time the experiment is a success (k <= n)
		param p: probability a success occurs
		'''

		factory_    = StatisticalIndexes()
		combination = factory_.Combination(n, k)

		return combination * (p ** k) * ( (1 - p) ** (n - k) )


