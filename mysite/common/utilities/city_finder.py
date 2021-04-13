# Finds a city based on latitude and longitude
import scipy
from scipy.spatial import KDTree
import csv, os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
WORLD_CITIES_DICT = {}
WORLD_CITIES_COORDS = []

class City:
    '''
    City wraps up the info about a city, including its name, coordinates,
    and belonging country.
    '''
    def __init__(self, city_name, country_code, admin_name):
        self.city_name = city_name
        self.country_code = country_code
        self.admin_name = admin_name
    def __str__(self):
        return f'{self.city_name},{self.admin_name}. {self.country_code}'

with open(os.path.join(__location__,'worldcities.csv'), 'r', encoding='utf-8') as csv_file:
    cities = csv.reader(csv_file)
        # discard the headers
    cities.__next__()

    # populate geo points into kdtree
    for city in cities:
        city_coordinate_key = (float(city[1]), float(city[2]))
        WORLD_CITIES_COORDS.append(city_coordinate_key)
        c = City(city[0], city[3],city[4])
        WORLD_CITIES_DICT[city_coordinate_key] = c

def find_city(latitude, longitude):
    _world_cities_kdtree = KDTree(WORLD_CITIES_COORDS,2)
    dd, ii = _world_cities_kdtree.query((latitude, longitude))
    return WORLD_CITIES_DICT[WORLD_CITIES_COORDS[ii]]
if __name__=='__main__':
    _world_cities_kdtree = KDTree(WORLD_CITIES_COORDS,2)
    dd, ii = _world_cities_kdtree.query((39.9700,-82.7906))
    print(dd,ii)
    print(WORLD_CITIES_DICT[WORLD_CITIES_COORDS[ii]])
