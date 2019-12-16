import pytest
import requests 

url = 'https://host-979tym.api.swiftype.com'
header = {'Authorization': 'Bearer private-xe2444z6g5jmvnevvyzkbkdv'}
engine = 'loe-promotions'

def test_conection_list_documents():
    r = requests.get(url + '/api/as/v1/engines/' + engine + '/documents/list', headers=header)
    assert r.status_code == 200

def test_conection_engine():
    r = requests.get(url + '/api/as/v1/engines/' + engine , headers=header)
    assert r.status_code ==  200