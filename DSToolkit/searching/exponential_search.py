import sys
from pathlib import Path


#############################################
root_path = Path(__file__).parents
sorting_  = str( root_path[1] ) + '/sorting/'

sys.path.append( sorting_ )
from quick_sort import *
#############################################


def exponential_search(el, arr:list=None) -> bool:

	'''
	Exponential Search
	'''

	return False