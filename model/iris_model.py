import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model.perceptron import Perceptron

class IrisModel:
    def __init__(self):
        self.iris = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None)
        print(self.iris.head())
        print('----------------------')
        print(self.iris.tail)
        print('----------------------')
        print(self.iris.columns)
        '''
        [150 rows x 5 columns]>
        ----------------------
        Int64Index([0, 1, 2, 3, 4], dtype='int64')
        '''

        # Iris-setosa 와 versicolor 선택 (MVC 는 이진분류만 할 수 있다)
        t = self.iris.iloc[0:100]
        self.y = np.where(t, 'Iris-setosa', -1, 1)
        # 꽃받침 길이, 꽃잎 추출
        self.x = self.iris.iloc[0:100, [0,2]].values
        self.clf = Perceptron(eta=0.1, n_iter=10)

    def get_iris(self):
        return self.iris

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw_scatter(self):
        X = self.x
        plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
        plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
        plt.xlabel('sepal length[cm]')
        plt.ylabel('petal length[cm]')
        plt.legend(loc='upper left')
        plt.show()

    def draw_errors(self):
        X = self.x
        y = self.y
        self.clf.fit(X, y)
        plt.plot(range(1, len(self.clf.errors_) + 1), self.clf.errors_, marker='o')
        plt.xlabel('Epoch')
        plt.ylabel('Number of Errors')
        plt.show()