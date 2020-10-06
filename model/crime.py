'''
서울시에서의 의뢰

과거의 구별 CCTV 데이터로 -> 2018년 구별 CCTV 설치 수 예측
=> 범죄율에 따른 CCTV 최적화된 수량 예측,
   구별로 충분량, 부족량인지를 판단해서 CCTV 할당량 예측
'''

'''
import pandas as pd 
import numpy as np

class Crime:

    def __init__(self):
        pass    

    def cctv_seoul_func(self):
        cctv_seoul = pd.read_csv('./data/cctv_in_seoul.csv')
        print(cctv_seoul.head())
        #print(cctv_seoul.columns)
        #print(cctv_seoul.columns[0])

        print('#'*50)
        print(cctv_seoul.sort_values(by='소계',ascending=True))
        
        print('#'*50)
        crime_seoul = pd.read_csv('./data/crime_in_seoul.csv')
        print(crime_seoul.head())

if __name__ == '__main__':
    test = Crime()
    test.cctv_seoul_func()
'''

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader

class CrimeModel:
    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader()

    def get_crime(self):
        reader = self.reader
        reader.context = os.path.join(baseurl, 'data')
        reader.fname = 'crime_in_seoul.csv'
        reader.new_file()
        crime = reader.csv_to_dframe()
        print(f'{crime.head()}')

if __name__ == '__main__':
    crime = CrimeModel()
    crime.get_crime()