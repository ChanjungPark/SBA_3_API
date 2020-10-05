import pandas as pd
import numpy as np

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
        self.x = self.iris.iloc[0:100, [0,2].value]