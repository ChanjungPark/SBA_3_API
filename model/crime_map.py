import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
from model.police import Police
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
        reader.fname = 'usa_map.json'
        reader.new_file()
        usa_map = reader.json_load()
        reader.fname = 'us_unemployment.csv'
        reader.new_file()
        us_unemployment = reader.csv_to_dframe()
        print(f'{us_unemployment.head()}')

        # 지도 그리기
        map = folium.Map(location=[37, -102], zoom_start=5)
        map.choropleth(
            geo_data = usa_map,
            name = 'choropleth',
            data = us_unemployment,
            columns = ['State', 'Unemployment'],
            key_on = 'feature.id',
            fill_color = 'YlGn',
            fill_opacity = 0.7,
            line_opacity = 0.2,
            legend_name = 'Unemployment Rate (%)'
        )
        folium.LayerControl().add_to(map)
        reader = self.reader
        reader.context = os.path.join(baseurl, 'data')
        reader.fname = 'usa.html'
        map.save(reader.new_file())

if __name__ == '__main__':
    us = CrimeMap()
    us.show_map()