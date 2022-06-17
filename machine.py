

'''
    
This file contains all the code that will run the machine learning
algorithm PCA.

'''

'''
We are making a class for the machine, which will learn using a given
data set.

Attributes:
 - machine.results
 - machine.figures
 - machine.model
 
Methods:
 - machine.learn()
 - machine.test()
 - machine.compare()
'''


#import packages
import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
#begin setting up class
class Machine(data):

    #init the class with parameters
    def __init__(self,data):
        self.testdata = data.testset
        self.traindata = data.trainset
        self.results = "No results made yet"
        self.figures = "No figured made yet"
        self.model = "No model made yet"
        self.score = 0


    ##make some methods

    #train the data using the training data - return model
    #We run the algorithm for a given data set and returns
    #a model for the data.
    def train(self,data):
        temp = pd.data.trainset.to_numpy()
        Y = temp[-1] # last column as "labels"
        X = temp[0:3] # not the last column

        #run lasso regression, get the model
        lasso = Lasso(alpha=0.1,max_iter=10)
        lasso.fit(X_train,y_train)

        #save results
        self.results = lasso.get_params()
        self.model = lasso
        self.score = lasso.score(X)
    def PCAlearn(self,data):
        decomposed=PCA(n_components=3) 
        normaldata=StandardScaler().fit_transform(data)
        return decomposed.fit_transform(normaldata)
#         print("The explained varience: ",decomposed.explained_variance_ratio_)
#         pipeline = Pipeline([('scaling', StandardScaler()), ('pca', PCA(n_components=3))])
#         pipeline.fit_transform(data)





















