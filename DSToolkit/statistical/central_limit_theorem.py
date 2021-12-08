###########################################################################################################
# The Central Limit Theorem states that THE SAMPLING DISTRIBUTION OF THE 
# SAMPLE MEANS IS DISTRIBUTED LIKE IF IT WERE A NORMAL DISTRIBUTION.
#
# To prove this visually, let's draw a generic distribution (i.e. exponential)
# and let's sample out of it means of a subsample. Once done, let's plot an
# histogram to see how the sample mean distribution is...
###########################################################################################################



import random
import numpy as np
import matplotlib.pyplot as plt



def sample_mean(x:list=None):
	
	return sum(x) / len(x)



# 1. Let's define a probability function that we assume we do not know as a population probability function...
def exponential(x=0, lamb=0, vector:list=None):

	if vector is not None:
		return [ exponential(x, lamb, vector=None) for x in vector ]
	else:
		return lamb * np.exp( -lamb * x )



# 2. Let's get out from the exponential distribution all the mean we may need...
mother_dist = exponential( lamb=0.1, vector = [ x  for x in range(0, 1000) ] )
sample_size = 450
extractions = 7500

sample_mean_extractions = [ sample_mean( random.sample(mother_dist, sample_size) ) for x in range(extractions) ]


# 3. Let's plot the sampling distribution of the sample mean to see how it goes ! 
plt.hist( sample_mean_extractions, bins = 50, edgecolor='black' )
plt.vlines( sample_mean(sample_mean_extractions), ymin=0, ymax=450, color='red' )
plt.show()


# Well, how does it look like the sampling distribution of the sample mean ?! I hope a "bell" rings inside you ! 
# Try to increase the "extractions" parameters to see how it goes...

