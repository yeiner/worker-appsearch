import pytest
import requests 

url = 'https://host-2je4fy.api.swiftype.com'
header = {'Authorization': 'Bearer private-xnv4gm2rwyhxhbzzba8y827o'}
engine = 'loe-promotions'

def test_conection_list_documents():
    r = requests.get(url + '/api/as/v1/engines/' + engine + '/documents/list', headers=header)
    assert r.status_code == 200

def test_conection_engine():
    r = requests.get(url + '/api/as/v1/engines/' + engine , headers=header)
    assert r.status_code ==  200
