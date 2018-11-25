import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
from matplotlib import pyplot as plt

iris = load_iris()
print(iris.data[:3], "\n")
print(iris.data[15:18], "\n")
print(iris.data[37:40], "\n")

print("We extract only the lengths and widths of the petals:")
X = iris.data[:, (2, 3)]

'''
iris.label contains the labels 0,1,2 corresponding 3 species of flowers; 
iris setosa,iris virginica,iris versicolor
'''
print(iris.target, "\n")

print("We turn the 3 classes into two classes, i.e: iris setosa not iris"
      " setosa (this means iris virginia or iris versicolor)")
y = (iris.target == 0).astype(np.int8)
print(y, "\n")

'''
In machine learning, the Perceptron is an algorithm for supervised learning of binary classifiers.
Perceptron is a linear classifier (binary)
Perceptron can be single layer or a multi-layer (Neural Networks). 
For multi layer Perceptron we use Backpropogation 
'''
print("We now create a Perceptron and fit the data X and y:")
p = Perceptron(random_state=42,
              max_iter=10)
p.fit(X, y)
print(p)

# Predictions
values = [[1.5, 0.1], [1.8, 0.4], [1.3, 0.2]]
for value in X:
    pred = p.predict([value])
    print([pred])

'''Multi-layer Perceptron We will continue with examples using the multilayer perceptron (MLP). 
The multilayer perceptron (MLP) is a feedforward artificial neural network model that maps sets of 
input data onto a set of appropriate outputs. An MLP consists of multiple layers and each layer is 
fully connected to the following one. The nodes of the layers are neurons using nonlinear activation 
functions, except for the nodes of the input layer. There can be one or more non-linear 
hidden layers between the input and the output layer.'''

from sklearn.neural_network import MLPClassifier
X = [[0., 0.], [0., 1.], [1., 0.], [1., 1.]]
y = [0, 0, 0, 1]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
print(clf.fit(X, y))

'''
The attribute coefs_ contains a list of weight matrices for every layer. 
The weight matrix at index i holds the weights between the layer i and layer i + 1.
'''

print("Weights between input and first hidden layer:")
print(clf.coefs_[0])
print("\nweights between first hidden and second hidden layer:")
print(clf.coefs_[1])

# the values of w0 and w1:
print("w0 = ", clf.coefs_[0] [0] [0])
print("w1 = ", clf.coefs_[0] [1] [0])

# the weight vector H00 can be accessed with:
print("\nweight vector of H00: ",clf.coefs_[0][:,0])

# Accessing a neuron Hij
print("\nWe can generalize the above to access a neuron Hij like so:", end="")
for i in range(len(clf.coefs_)):
    number_neurons_in_layer = clf.coefs_[i].shape[1]
    for j in range(number_neurons_in_layer):
        weights = clf.coefs_[i][:,j]
        print(i, j, weights, end=", ")
        print()
    print()

# Intercepts_ is a list of bias vectors, where
# the vector at index i represents the bias values added
# to layer i + 1
print("Bias values for first hidden layer:")
print(clf.intercepts_[0])
print("\nBias values for second hidden layer:")
print(clf.intercepts_[1])

result = clf.predict([[0, 0], [0, 1],
                     [1, 0], [0, 1],
                     [1, 1], [2., 2.],
                     [1.3, 1.3], [2, 4.8]])

prob_results = clf.predict_proba([[0, 0], [0, 1],
                                 [1, 0], [0, 1],
                                 [1, 1], [2., 2.],
                                 [1.3, 1.3], [2, 4.8]])
print('res: ',result)
print('prob_results: ', prob_results)

# Example 2

npoints = 50
X, Y = [], []

# class 0
X.append(np.random.uniform(low=-2.5, high=2.3, size=(npoints,)))
Y.append(np.random.uniform(low=-1.7, high=2.8, size=(npoints,)))

# class 1
X.append(np.random.uniform(low=-7.2, high=-4.4, size=(npoints,)))
Y.append(np.random.uniform(low=3, high=6.5, size=(npoints,)))
learnset = []
learnlabels = []