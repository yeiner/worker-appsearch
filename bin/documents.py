import configparser
from elastic_app_search import Client
import requests
import json
import pdb
import sys
from .command_base import CommandBase


#config = configparser.ConfigParser()
#config.read('../config/config.ini')

#host_identifier = config['DEFAULT']['HOST_IDENTIFIER']
host_identifier = 'host-2je4fy'
api_key = 'private-xnv4gm2rwyhxhbzzba8y827o'
#api_key = config['DEFAULT']['BEARER']
engine_name = 'loe-promotions'


class Documents(CommandBase):

    def __init__(self, arguments):
        super(Documents, self).__init__(arguments)
        self.host_identifier = host_identifier
        self.api_key = api_key
        self.engine_name = engine_name
    
    def exe_command(self):
        print('----Inicia el Documents----')
        if self.arguments['delete'] is True:
            print('----Delete all Documents----')
            self.delete_documents()
        if self.arguments['create'] is True:
            print('----Create all Documents----')
            self.create_document()
        if self.arguments['dump'] is True:
            print('----Dump all Documents----')
            self.get_dummy()

    def create_document(self):
        client = Client(self.host_identifier, self.api_key)
        r = requests.get('https://api.myjson.com/bins/11s4jg')
        data = r.json()

        response = client.index_documents(self.engine_name, data)
        print('Created docuemnts')
        print(response)
    
    def get_dummy(self):
        r = requests.get('https://api.myjson.com/bins/11s4jg')
        data = r.json()
        with open('data.json', 'w') as f:
            json.dump(data, f)
    
    def delete_documents(self):
        client = Client(self.host_identifier, self.api_key)
        """Get documents """
        documents = client.list_documents(self.engine_name)
        """ Iteration ids """
        ids = [elment['id'] for elment in documents['results']]
        print(ids)
        """ Delete docuemnts """
        response = client.destroy_documents(self.engine_name, ids)
        print('delete docuemnt')
        print(response)
