########################################################################################################################
# LOGISTIC REGRESSION IS A BINARY CLASSIFICATION MODEL SOLVER !
# ...IT IS USED TO PREDICT A BINARY OUTCOME FROM A LINEAR COMBINATION OF VARIABLES (CLASS 0 AND CLASS 1)...
# FIRST STEP: GET THE PROBABILITY OF CLASSIFYING CLASS 1
# SECOND STEP: PREDICT THE CLASS BASED ON PROBABILITY AND THRESHOLDS
# IN ORDER TO GET "BETAS" FOR THE LINEAR COMBINATION WE ARE GOING TO USE THE MAXIMUM LIKELIHOOD FUNCTION:
# ---> WE NEED TO ESTIMATE BETAS TO MAXIMIZE THE LIKELIHOOD...
#
# THE LIKELIHOOD FUNCTION IS THE ONE THAT FOLLOWS:
# LOG(L(BETA)) = LOG( PRODUTTORIA_I_M( P(Xi)**Yi * (1 - P(Xi))**(1 - Yi) ) ) =
#              = SUM_I_M( Yi * LOG(P(Xi)) + (1 - Yi) * LOG( 1- P(Xi) ) )  <---- LOG LIKELIHOOD FUNCTION !
########################################################################################################################


from sklearn.linear_model import LogisticRegression
from tqdm import tqdm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import os


#dataset = pd.read_csv(os.getcwd() + '/Codes/logistic_regression_dataset.csv', sep=',')


def initalize_params(n):
        beta_0     = 0
        beta_other = [random.random() for _ in range(n)]
        return beta_0, beta_other


def logistic_function_np(point, beta_0, beta_other):

    return 1 / 1 + np.exp( -(beta_0 + point.dot(beta_other)) )


def compute_gradients(x, y, beta_0, beta_other, m, n):

    gradient_beta_0     = 0
    gradient_beta_other = [0] * n

    for i, point in enumerate(x):
        pred = logistic_function_np(point, beta_0, beta_other)
        for j, feature in enumerate(point):
            gradient_beta_other[j] += ((pred - y[i]) * feature) / m # THIS IS THE GRADIENT UPDATES !!!
        gradient_beta_0 += (pred - y[i]) / m

    return gradient_beta_0, gradient_beta_other


def update_params(beta_0, beta_other, gradient_beta_0, gradient_beta_other, learning_rate):

    beta_0 -= gradient_beta_0 * learning_rate
    for i in range(len(beta_other)):
        beta_other[i] -= gradient_beta_other[i] * learning_rate

    return beta_0, beta_other


def logistic_regression(x, y, iterations=250, learning_rate=0.000000001):

    m, n = len(x), len(x[0])
    beta_0, beta_other = initalize_params(n)

    for _ in tqdm(range(iterations)): # Iterations are called epochs...
        gradient_beta_0, gradient_beta_other = compute_gradients(x, y, beta_0, beta_other, m, n)
        beta_0, beta_other = update_params(beta_0, beta_other, gradient_beta_0, gradient_beta_other, learning_rate)

    return beta_0, beta_other



#x      = dataset.drop('target', axis = 1).values
#y      = dataset[['target']].values
#coeff_ = logistic_regression(x, y)
#print(coeff_)


#clf = LogisticRegression(max_iter=1000).fit(x, y)
#print(clf.coef_)




