import configparser
from elastic_app_search import Client
import requests
import json
import pdb

#config = configparser.ConfigParser()
#config.read('../config/config.ini')

#host_identifier = config['DEFAULT']['HOST_IDENTIFIER']
host_identifier = 'host-2je4fy'
api_key = 'private-xnv4gm2rwyhxhbzzba8y827o'
#api_key = config['DEFAULT']['BEARER']
engine_name = 'loe-promotions'


class Documents():

    def create_document():

        client = Client(host_identifier, api_key)
        r = requests.get('https://api.myjson.com/bins/11s4jg')
        data = r.json()

        response = client.index_documents(engine_name, data)
        print('Created docuemnts')
        print(response)
    
    def get_dummy():
        r = requests.get('https://api.myjson.com/bins/11s4jg')
        data = r.json()
        with open('data.json', 'w') as f:
            json.dump(data, f)
    
    def delete_documents():
        client = Client(host_identifier, api_key)
        """Get documents """
        documents = client.list_documents(engine_name)
        """ Iteration ids """
        ids = [elment['id'] for elment in documents['results']]
        print(ids)
        """ Delete docuemnts """
        response = client.destroy_documents(engine_name, ids)
        print('delete docuemnt')
        print(response)



if __name__ == '__main__':
    Documents.create_document()
