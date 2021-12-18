import requests
import json


url = "https://api.zippopotam.us/PL/84-240"
head = {'content-type': 'application/json'}
response = requests.request("GET", url)
a = json.loads(response.text)

expected = ['post code', 'country', 'country abbreviation', 'places']
current = []

for key, value in a.items():
        if key in expected:
            current.append(key)
assert expected == current

def test_get_data_of_loacation_Reda_equals_200():
    response = requests.get("https://api.zippopotam.us/PL/84-240")
    assert response.status_code == 200


print(response.json())



def test_get_data_of_loacation_Reda_equals_json():
    response = requests.get("https://api.zippopotam.us/PL/84-240")
    assert response.headers["Content-Type"] == "application/json"


def test_get_data_of_post_code_Reda_equals_84240():
    response = requests.get("https://api.zippopotam.us/PL/84-240")
    response_body = response.json()
    assert response_body["post code"] == "84-240"


def test_get_data_of_loacation_country_Reda_equals_poland():
    response = requests.get("https://api.zippopotam.us/PL/84-240")
    response_body = response.json()
    assert response_body["country"] == "Poland"



def test_get_data_of_loacation_country_abbreviation_Reda_equals_pl():
    response = requests.get("https://api.zippopotam.us/PL/84-240")
    response_body = response.json()
    assert response_body["country abbreviation"] == "PL"


def test_get_data_of_loacation_city_Reda_equals_Reda():
    response = requests.get("https://api.zippopotam.us/PL/84-240")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Reda"


def test_get_data_of_loacation_state_Reda_equals_pomorskie():
    response = requests.get("https://api.zippopotam.us/PL/84-240")
    response_body = response.json()
    assert response_body["places"][0]["state"] == "Pomorskie"

def test_get_data_of_loacation_Reda_one_place_is_returned():
    response = requests.get("https://api.zippopotam.us/PL/84-240")
    response_body = response.json()
    assert len(response_body["places"]) == 1

def test_get_data_of_loacation_Reda_fail():
    response = requests.get("https://api.zippopotam.us/PL/84-240")
    response_body = response.json()
    assert len(response_body["places"]) == 2

def test_post():
    url = 'https://jsonplaceholder.typicode.com/posts'

    headers = {'Content-Type': 'application/json; charset=UTF-8'}

    payload = {'title': 'foo',
    'body': 'bar',
    'userId': 1}

    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

    assert resp.status_code == 201
    resp_body = resp.json()
    assert resp_body['title'] == 'foo'
    assert resp_body['body'] == 'bar'
    assert resp_body['userId'] == 1

def test_put():
    url = 'https://jsonplaceholder.typicode.com/posts/1'

    headers = {'Content-Type': 'application/json; charset=UTF-8'}

    payload = {'id': 2,
    'title': 'foof',
    'body': 'barb',
    'userId': 10}

    resp = requests.put(url, headers=headers, data=json.dumps(payload, indent=4))

    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['id'] == 1
    assert resp_body['title'] == 'foof'
    assert resp_body['body'] == 'barb'
    assert resp_body['userId'] == 10
