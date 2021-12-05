import math
import random
import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt


########################################################################################################################
# COMMON SAMPLING METHODS ARE:
# ---> SAMPLING IS GENERATING RANDOM VARIABLES OUT OF A PROBABILITY DISTRIBUTION F
# . IMPORTANCE  SAMPLING
# . REJECTION   SAMPLING
# . INVERSE     SAMPLING
# . WEIGTHED    SAMPLING
# . RESERVOIR   SAMPLING


########################################################################################################################
# 1.0. REJECTION SAMPLING
# Rejection sampling builds an overlaying distribution [f(x)] over a complex distribution function...
# After this building overlaying function [g(x)], we get x out of g(x) and we sample uniformly between 0 and g(x)...
# If the value we obtain (i.e. U) respects the following criteria which is U(0, g(x)) > f(x) we REJECT the observation...

# This is my "crazy" function...
def _f(x):
    if x < -2:
        return 0
    elif x < 0:
        return sp.norm.pdf(x, loc=0, scale=1)
    elif x < 2:
        return 0.2 * np.sqrt(x)
    elif x < 4:
        return 0.11 * np.log(x)
    else:
        return 0

f = np.vectorize(_f, otypes=[np.float])

y = np.linspace(-5, 5)
plt.figure(figsize=(15, 10))
plt.bar(y, f(y))


# Define overlaying distribution...
(a, b) = (-5, 5)

def _g(x):
    return sp.uniform.pdf(x, loc=a, scale=b - a)

g = np.vectorize(_g, otypes=[np.float])

plt.bar(y, g(y))
plt.xlim(-7, 7)


################################################################################################
# Calculate the M factor !!!!!!!!!!!!! Most important things is to get correct scaling factor...
M = max( f(y) / g(y) )
plt.figure(figsize=(10, 5))
plt.plot(y, M * g(y), label='M * g(y)')
plt.plot(y, f(y), label='f(x)')
plt.xlim(-7, 7)
plt.legend(loc='best')


# Vanilla implementation...
X = []
n = 10_000

for i in range(n):
    x = np.random.uniform(a, b)
    if f(x) / (M * g(x)) < random.random():
        X.append( x )

print('Accepted samples: {}'.format(len(X)))
print('Accepted ratio: {}'.format(100 * len(X) / n))






########################################################################################################################
# 1.1. REJECTION SAMPLING
# Rejection sampling builds an overlaying distribution [f(x)] over a complex distribution function...
# After this building overlaying function [g(x)], we get x out of g(x) and we sample uniformly between 0 and g(x)...
# If the value we obtain (i.e. U) respects the following criteria which is U(0, g(x)) > f(x) we REJECT the observation...


import random

probability_distribution = [{"value": 1, "probability": 0.1},
                            {"value": 5, "probability": 0.7},
                            {"value": 8, "probability": 0.2}]

def draw_from_non_uniform_distribution(probability_distribution):
    r_value, r_probability, accept = 0, 0, 0
    members = len(probability_distribution)

    while not accept:

        bin = random.choice(range(members))
        binned_object = probability_distribution[bin]
        r_value = binned_object['value']
        r_probability = binned_object['probability']

        if random.random() <= r_probability:
            accept = 1

    return r_value

bins = {}
total_draws = 10_000

for i in range(total_draws):

    r_value = draw_from_non_uniform_distribution(probability_distribution)

    if (bins.get(r_value) != None):
        bins[r_value] += 1
    else:
        bins[r_value] = 1

print(bins)






