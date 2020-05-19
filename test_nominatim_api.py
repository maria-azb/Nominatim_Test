import requests
import pytest

api_url_search = "https://nominatim.openstreetmap.org/search"
api_url_reverse = "https://nominatim.openstreetmap.org/reverse"

right_search_results = {
	'Kremlin and Red Square, Moscow': [55.7520439, 37.61850028109701],
	'Platz der Republik 1, Berlin': [52.51865325, 13.37610135409873],
	'Pennsylvania Ave NW, Washington': [38.9018853, -77.0482619],
	'Parliament House, Melbourne': [-37.811128350000004, 144.97384637540324],
	'Soul Buoy': [0, 0]
}
right_reverse_results = {
	'55.7520439, 37.61850028109701': 'Московский Кремль и Красная Площадь, Боровицкая улица, 28, Старое Ваганьково, Москва, Центральный административный округ, Москва, Центральный федеральный округ, 121019, Россия',
	'52.51865325, 13.37610135409873': 'Reichstagsgebäude, 1, Platz der Republik, Tiergarten, Mitte, 10557, Deutschland',
	'38.9018853, -77.0482619': 'International Finance Corporation, 2121, Pennsylvania Avenue Northwest, Washington, District of Columbia, 20006, United States of America',
	'-37.811128350000004, 144.97384637540324': 'Parliament House, Spring Street, East Melbourne, City of Melbourne, Victoria, 3000, Australia',
	'0, 0': 'Soul Buoy'
}

params_search = [
{
    'q': 'Kremlin and Red Square, Moscow',
    'format': 'json'
},
{
    'q': 'Platz der Republik 1, Berlin',
    'format': 'json'
},
{
    'q': 'Pennsylvania Ave NW, Washington',
    'format': 'json'
},
{
    'q': 'Parliament House, Melbourne',
    'format': 'json'
},
{
    'q': 'Soul Buoy',
    'format': 'json'
}
]

params_reverse = [
{
    'lat': '55.7520439',
    'lon': '37.61850028109701',
    'format': 'json'
},
{
    'lat': '52.51865325',
    'lon': '13.37610135409873',
    'format': 'json'
},
{
    'lat': '38.9018853',
    'lon': '-77.0482619',
    'format': 'json'
},
{
    'lat': '-37.811128350000004',
    'lon': '144.97384637540324',
    'format': 'json'
},
{
    'lat': '0',
    'lon': '0',
    'format': 'json'
}
]

@pytest.mark.parametrize('params', params_search)
def test_search_coordinates_by_address(params):

    response = requests.get(api_url_search, params=params).json()
    lat = float(response[0]['lat'])
    lon = float(response[0]['lon'])
    assert (lat == right_search_results[params['q']][0]) & (lon == right_search_results[params['q']][1]), "Incorrect coordinates"
	
@pytest.mark.parametrize('params', params_reverse)
def test_search_address_by_coordinates(params):

    response = requests.get(api_url_reverse, params=params).json()
    address = response['display_name']
    assert (address == right_reverse_results[params['lat'] + ", " + params['lon']]), "Incorrect address"	
	