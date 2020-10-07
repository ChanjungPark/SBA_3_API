import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
from model.police import Police
from model.crime import CrimeModel
import folium

class CrimeMap:
    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader()

    def hook_process(self):
        police = Police()
        police_norm = police.get_police_norm()

    def create_seoul_crime_map(self):
        reader = self.reader
        reader.context = os.path.join(baseurl, 'data')
        reader.fname = 'seoul_map.json'
        reader.new_file()
        seoul_map = reader.json_load()
        reader.fname = 'police_norm.csv'
        reader.new_file()
        police_norm = reader.csv_to_dframe()
        crimeModel = CrimeModel()
        crime = crimeModel.get_crime()
        print(f'{police_norm.head()}')
        

        # 지도 그리기

        map = folium.Map(location=[37.5502, 126.982], zoom_start=12)
        map.choropleth(
            geo_data = seoul_map,
            name = 'choropleth',
            data = police_norm,
            columns = ['구별', '살인검거율'],
            key_on = 'feature.id',
            fill_color = 'YlGn',
            fill_opacity = 0.7,
            line_opacity = 0.2,
            legend_name = '살인검거율 (%)'
        )
        folium.LayerControl().add_to(map)
        reader = self.reader
        reader.context = os.path.join(baseurl, 'saved_data')
        reader.fname = 'police.html'
        map.save(reader.new_file())

if __name__ == '__main__':
    crime = CrimeMap()
    crime.create_seoul_crime_map()