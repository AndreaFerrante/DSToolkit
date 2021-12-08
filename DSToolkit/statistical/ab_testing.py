########################################################################################################################
# BAYESIAN INTUITIONS...
# We update our prior belief with evidence (update a prior belief with new information coming in !)
########################################################################################################################


import numpy as np
import pandas as pd
from scipy.stats import beta, gamma
from numpy.random import randn
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


plt.style.use('seaborn')
warnings.filterwarnings("ignore")
np.random.seed(42)


# ---> Beta (alpha = # time you see a success, beta = # time you see a failure)
# Beta is the function I use to model my believes...


b2 = sns.distplot(beta.rvs(16, 84, size=10_000),
                  hist     = False,
                  color    = 'green',
                  label    = 'Confident - Beta (16, 84)')

b1 = sns.distplot(beta.rvs(8, 42, size=10_000),
                  hist     = False,
                  color    = 'red',
                  label    = 'Neutral - Beta (8, 42)')

b3 = sns.distplot(beta.rvs(4, 21, size=10_000),
                  hist     = False,
                  color    = 'orange',
                  label    = 'Sceptikal - Beta (4, 21)')

plt.legend(loc='best')
plt.ylabel('Density')
plt.xlabel('Click Rate')



########################################################################################################################
# Conduct the A/B testing....
group_size = 1000
A_group, B_group = np.random.randn(2, group_size)

A_success = sum(A_group < 0.15) # click rate of advertisement A...
B_success = sum(B_group < 0.2)  # click rate of advertisement B...

A_failure = group_size - A_success
B_failure = group_size - B_success

A_posterior = beta(A_success + 8, A_failure + 42)
B_posterior = beta(B_success + 8, B_failure + 42)

A_posterior_ = beta.rvs(A_success + 8, A_failure + 42, size=10_000)
B_posterior_ = beta.rvs(B_success + 8, B_failure + 42, size=10_000)

a = sns.distplot(A_posterior_,
                 hist   = False,
                 color  = 'blue',
                 label  = 'A - Variant')

b = sns.distplot(B_posterior_,
                 hist   = False,
                 color  = 'green',
                 label  = 'B - Variant')

plt.legend(loc='best')
plt.ylabel('Density')
plt.xlabel('Click Rate')


########################################################################################################################
# Do Montecarlo simulation...
n_trials  = 10_000
A_samples = pd.Series([A_posterior.rvs() for _ in range(n_trials)])
B_samples = pd.Series([B_posterior.rvs() for _ in range(n_trials)])
B_wins    = sum(B_samples > A_samples)

B_wins / n_trials