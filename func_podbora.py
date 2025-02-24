import requests
def get_map_params(place):
    params = {'apikey':'8013b162-6b42-4997-9691-77b7074026e0', "geocode": place, "format": "json"}
    map_api = "http://geocode-maps.yandex.ru/1.x/"
    
    response = requests.get(map_api, params=params)
    return response

def get_map_photo(place, point1, point2):
    point1 = ','.join(point1)
    point2 = ','.join(point2)
    map_params = {
    "ll": ','.join(place),
    "apikey": "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13",
    # "spn": '0.019,0.019',
    # toponym_coodrinates2 = ','.join(toponym_coodrinates2)
    "pt": f'{point1},pm2rdm~{point2},pm2rdm',
    }
    map_api_server = "https://static-maps.yandex.ru/v1"

    response = requests.get(map_api_server, params=map_params)
    return response

def get_map_placec(place, text):
    map_params = {
          "apikey": 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3',
            "text": text,
            "lang": "ru_RU",
            "ll": f'{place[0]},{place[1]}',
            "spn": '1,1',
            "type": "biz"}
    
    search_api_server = "https://search-maps.yandex.ru/v1/"

    response = requests.get(search_api_server, params=map_params)

    return response
