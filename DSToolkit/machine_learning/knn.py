########################################################################################################################
# A new datapoint is determined (regression and classification) by its closest neighbors
# To make a prediction we need to find the distance between a new datapoint and ALL the datapoint into our dataset:
#  ---> REGRESSION: we take the average of all datapoints
#  ---> CLASSIFICATION: we take the counting of all its datapoints
# In order to determine the best K hyperparamter we could:
#  1. Get the square root of the number of datapoints we have in our training dataset
#  2. Perform a cross validation
########################################################################################################################


from collections import Counter


class KNN(object):

    def __init__(self):
        self.x = None
        self.y = None

    def euclidean_distance(self, point_1, point_2):
        return ( (point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2 )**0.5

    def train(self, x, y):
        self.x = x # This is in the form of a matrix x[n, m]: x=num. of datapoints, m=num. of features...
        self.y = y # This is the class or the values we would like to get...

    def predict(self, x, k, type='classification'):

        distances = []
        for point, label in zip(self.x, self.y):
            distance = self.euclidean_distance(point, x)
            distances.append( (distance, label) ) # add tuples to sort by the first index in sorted python function !

        neighbors = sorted(distances)[:k]

        if type != 'classification':
            return sum( label for _, label in neighbors )/k # This is the average if the problem is a regression one...
        else:
            return Counter(neighbors).most_common()[0][0] # This is the most common label if the problem is a classification one...




