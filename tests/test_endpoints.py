import pytest
import requests
import configparser
from pathlib import Path

path_config_file = Path.cwd() / 'config' / 'config.ini'
config = configparser.ConfigParser()
config.read(str(path_config_file))
host_identifier = config['TESTING']['HOST_IDENTIFIER']
host_appsearch = config['TESTING']['HOST_APPSEARCH']
api_key = config['TESTING']['BEARER']
engine_name = config['TESTING']['ENGINE_NAME']

url = 'https://' + host_identifier + '.' +  host_appsearch
header = {'Authorization': 'Bearer ' + api_key}


def test_conection_list_documents():
    r = requests.get(url + '/api/as/v1/engines/' + engine_name + '/documents/list', headers=header)
    assert r.status_code == 200

def test_conection_engine():
    r = requests.get(url + '/api/as/v1/engines/' + engine_name , headers=header)
    assert r.status_code ==  200
