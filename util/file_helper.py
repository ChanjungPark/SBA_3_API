from dataclasses import dataclass
import pandas as pd
import os
import xlrd
import googlemaps

'''
pandas version 1.x 이상 encoding='UTF-8' 불필요
ImportError: Missing optional dependency 'xlrd'
-> 아나콘다 프롬프트에서 pip install xlrd
   (주의!! conda install xlrd 하면 X)
'''

@dataclass
class FileReader:
    # def __init__(self, context, fname, train, test, id, label):
    #     self._context = context  # _ 1개는 default 접근, _ 2개는 private 접근

    # 3.7부터 간소화되서 dataclass 데코 후, key: value 형식으로 써도 됨 (롬복 형식)
    context : str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id : str = ''
    lable : str = ''

    def new_file(self) -> str:
        return os.path.join(self.context, self.fname)

    def csv_to_dframe(self) -> object:
        return pd.read_csv(self.new_file(), encoding='UTF-8', thousands=',')

    def xls_to_dframe(self, header, usecols) -> object:
        print(f'PANDAS VERSION: {pd.__version__}')
        return pd.read_excel(self.new_file(), header=header, usecols=usecols)
        
    def create_gmaps(self):
        return googlemaps.Client(key='')  # 개인 구글맵 api key 넣으면 된다