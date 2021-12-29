from factory import *
import numpy as np

import sys
from pathlib import Path


#############################################
root_path = Path(__file__).parents
sorting_  = str( root_path[1] ) + '/sorting/'

sys.path.append( sorting_ )
from quick_sort import *
#############################################


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
		Spearman correlation index is a non-parametric index for correlations.
		This correlation index wants the variables to be sortable since it performs correlation measuring 
		the rank of the variables. 
		Differently from Pearson correlation index, Spearman correlation index measures how well 
		the relationship between two variables could be described by a monotonic function.
		Practically, this index is nothing more than a sub-case of the Pearson correlation index 
		performed over ranks.

		param x: first list to analyze to see how much correlation is in place against y variable
		param y: second list to analyze to see how much correlation is in place against x variable
		'''

		SI         = StatisticalIndexes()

		x_rank     = SI.Ranker(x) # Rank x array...
		y_rank     = SI.Ranker(y) # Rank y array...

		covariance = SI.Covariance(x_rank, y_rank)
		dev_std_x  = SI.StandardDeviationSample(x_rank)
		dev_std_y  = SI.StandardDeviationSample(y_rank)

		return round(covariance / (dev_std_x * dev_std_y), 9)
		

	def KendallCorrelation(self, x:list, y:list):

		'''
		'''

		pass



x = [12,14,19,16]
y = [13,15,16,17]

from scipy.stats import spearmanr

s  = StatisticalIndexes()
si = Correlations()

print('Spearman mine',  si.SpearmanCorrelation(x, y))
print('Spearman scipy', spearmanr(x, y))



