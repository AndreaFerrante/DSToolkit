########################################################################################################################
# BUILDING LINEAR REGRESSION FROM SCRATCH
# ...WE ARE GOING TO GET IT WITH THE MAIN + HELPER FUNCTIONS METHOD...
# ...WE ARE GOING TO MINIMIZE THE MEAN SQUARED ERROR (ORDINARY LEAST SQUQARES): THIS IS OUR LOSS FUNCTION...
# ...WITH GRADIENT DESCENT WE MINIMIZE THE ERROR OVER DIFFERENT ITERATIONS...
########################################################################################################################


from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import os


#dataset = pd.read_csv(os.getcwd() + '/Codes/linear_regression_dataset.csv', sep = ',')
#dataset = dataset[['Head_Size', 'Brain_Weight']]


def initialize_params(dimensions):

    beta_0     = 0
    beta_other = [random.random() for _ in range(dimensions)]

    return beta_0, beta_other


def compute_gradient(x, y, beta_0, beta_other, dimensions, m):

    gradient_beta_0     = 0
    gradient_beta_other = [0] * dimensions

    for i in range(m):
        y_i_hat   = sum( [x[i][j] * beta_other[j] for j in range(dimensions)] ) + beta_0
        derror_dy = 2 * (y[i] - y_i_hat)

        for j in range(dimensions):
            gradient_beta_other[j] += (derror_dy * x[i][j]) / m
        gradient_beta_0 += derror_dy / m

    return gradient_beta_0, gradient_beta_other


def update_params(beta_0, beta_other, gradient_beta_0, gradient_beta_other, learning_rate):

    beta_0 += gradient_beta_0 * learning_rate
    for i in range(len(beta_other)):
        beta_other[i] += gradient_beta_other[i] * learning_rate

    return beta_0, beta_other


def linear_regression(x, y, epochs=750, learning_rate=0.00000000045):

    n, m = len(x[0]), len(x)
    beta_0, beta_other = initialize_params(n)

    for _ in range(epochs):
        gradient_beta_0, gradient_beta_other = compute_gradient(x, y, beta_0, beta_other, n, m)
        beta_0, beta_other = update_params(beta_0, beta_other, gradient_beta_0, gradient_beta_other, learning_rate)

    return beta_0, beta_other


#coeff = linear_regression(x = dataset[['Head_Size']].values, y = dataset[['Brain_Weight']].values )
#print(coeff)


#reg = LinearRegression().fit( dataset[['Head_Size']].values, dataset[['Brain_Weight']].values )
#print(reg.coef_, reg.intercept_)


########################################################################################################################
# PLOTTING...

#plt.scatter(dataset.Head_Size, dataset.Brain_Weight, edgecolors='black', label='Data Points')
#plt.xlabel('Head Size')
#plt.ylabel('Brain Weight')

#all_x = np.linspace(dataset[['Head_Size']].min(), dataset[['Head_Size']].max(), 2000)
#plt.plot(all_x, coeff[0] + coeff[1] * all_x, color='red', lw=2, label='Gradient Regression')
#plt.plot(all_x, reg.intercept_ + reg.coef_ * all_x, color='green', lw=2, label='Sklearn Regression')

#plt.legend(loc='best')
#plt.show()