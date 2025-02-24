from func_podbora import get_map_params, get_map_photo, get_map_placec
import requests 
import sys
import math
from io import BytesIO
from PIL import Image

adress = " ".join(sys.argv[1:])

# print(adress)

response = get_map_params(adress)

json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]

text = 'Аптека'

toponym_coodrinates = toponym_coodrinates.split(' ')

response2 = get_map_placec(toponym_coodrinates, text)

# print(response2.url)

json_response2 = response2.json()

toponym2 = json_response2["features"][0]['properties']['CompanyMetaData']

toponym_coodrinates2 = json_response2["features"][0]['geometry']['coordinates']

toponym_coodrinates2[0] = str(toponym_coodrinates2[0])
toponym_coodrinates2[1] = str(toponym_coodrinates2[1])
# toponym_coodrinates2 = ','.join(toponym_coodrinates2)
# toponym_coodrinates = ','.join(toponym_coodrinates)

toponym_coodrinates_srednee = [(float(toponym_coodrinates[0]) + float(toponym_coodrinates2[0])) / 2, (float(toponym_coodrinates[1]) + float(toponym_coodrinates2[1])) / 2]

toponym_coodrinates_srednee[0] = str(toponym_coodrinates_srednee[0])
toponym_coodrinates_srednee[1] = str(toponym_coodrinates_srednee[1])

response3 = get_map_photo(toponym_coodrinates_srednee, toponym_coodrinates, toponym_coodrinates2)

def calculate_distance(lon1, lat1, lon2, lat2):
    R = 6371.0  # Радиус Земли в километрах
    dlon = math.radians(lon2 - lon1)
    dlat = math.radians(lat2 - lat1)
    
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return distance

distance = calculate_distance(float(toponym_coodrinates[0]), float(toponym_coodrinates[1]), float(toponym_coodrinates2[0]), float(toponym_coodrinates2[1]))


print(distance)

im = BytesIO(response3.content)
opened_image = Image.open(im)
opened_image.show()

# python 3zadanie.py Москва, ул. Ак. Королева, 12
# python 3zadanie.py улица Академика Королёва, 21с1
