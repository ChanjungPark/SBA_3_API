'''
서울시에서의 의뢰

과거의 구별 CCTV 데이터로 -> 2018년 구별 CCTV 설치 수 예측
=> 범죄율에 따른 CCTV 최적화된 수량 예측,
   구별로 충분량, 부족량인지를 판단해서 CCTV 할당량 예측
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

    def hook_process(self):
        print('----------- CRIME & POLICE -----------')
        crime = self.get_crime()
        print(f'{crime.head()}')
        # self.get_station(crime)
        crime_police = self.get_crime_police()
        print(f'{crime_police.head()}')
        print(f'{crime_police.columns}')

    def get_crime(self):
        reader = self.reader
        reader.context = os.path.join(baseurl, 'data')
        reader.fname = 'crime_in_seoul.csv'
        reader.new_file()
        crime = reader.csv_to_dframe()
        # print(f'{crime.head()}')
        return crime

    def get_station(self, crime):
        reader = self.reader
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울'+str(name[:-1]+'경찰서'))
        station_addrs = []
        station_lats = []   # 위도
        station_lngs = []   # 경도
        gmaps = reader.create_gmaps()
        for name in station_names:
            t = gmaps.geocode(name, language='ko')
            station_addrs.append(t[0].get('formatted_address'))
            t_loc = t[0].get('geometry')
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])
            print(name + '----->' + t[0].get('formatted_address'))
        gu_names = []

        for name in station_addrs:
            t = name.split()
            gu_name = [gu for gu in t if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(crime.head())

        crime.loc[crime['관서명'] == '혜화서', ['구별']] == '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] == '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] == '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] == '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] == '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] == '강남구'

        print(crime.head())
        reader = self.reader
        reader.context = os.path.join(baseurl,'saved_data')
        reader.fname = 'crime_police.csv'
        crime.to_csv(reader.new_file())

    def get_crime_police(self):
        reader = self.reader
        reader.context = os.path.join(baseurl, 'saved_data')
        reader.fname = 'crime_police.csv'
        reader.new_file()
        crime_police = reader.csv_to_dframe()
        print(f'{crime_police.head()}')
        return crime_police

if __name__ == '__main__':
    crime = CrimeModel()
    # crime.get_crime()
    crime.hook_process()