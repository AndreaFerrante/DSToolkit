from .statistical_indexes import *
import numpy as np
import random


x = [1,3,6,10,11]
y = [1,3,6,10.5,11]


class Correlations(object):

	def __init__(self):
		super().__init__()


	def PearsonCorrelation(self, x:list, y:list):

		'''
		This correlation index is a linear correlation index. It goes from -1 till 1. This coefficient is ideal 
		when the two variables are linearly related.
		A correlation equal to -1 stands for perfect inverse correlation. A correlation index equal to 1 stands for
		a perfect positive correlation. Basically, Pearson correlation index is the ratio between covariance between 
		X and Y variables and multiplication between their standard deviation.

		param x: first list to analyze to see how much correlation is in place against y variable
		param y: second list to analyze to see how much correlation is in place against x variable
		'''

		SI         = StatisticalIndexes()

		covariance = SI.Covariance(x, y)
		dev_std_x  = SI.StandardDeviationSample(x)
		dev_std_y  = SI.StandardDeviationSample(y)

		return round(covariance / (dev_std_x * dev_std_y), 9)


	def SpearmanCorrelation(self, x:list, y:list):

		'''
		'''

		pass


si = Correlations()
print(si.PearsonCorrelation(x, y))
print(np.corrcoef(x, y))


