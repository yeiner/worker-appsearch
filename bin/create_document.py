import configparser
from elastic_app_search import Client 

#config = configparser.ConfigParser()
#config.read('../config/config.ini')

#host_identifier = config['DEFAULT']['HOST_IDENTIFIER']
host_identifier = 'host-979tym'
api_key = 'private-xe2444z6g5jmvnevvyzkbkdv'
#api_key = config['DEFAULT']['BEARER']
engine_name = 'loe-promotions'


class Documents():

    def create_document():

        client = Client(host_identifier, api_key)
        document = {
            "name": "test worker by",
            "id": 1217,
            "logo_premium": "http://cys.loe-seasons.local/promotion/1.jpg",
            "initial_price": "100000",
            "final_price": "50000",
            "discount": "50",
            "src_id": 1,
            "visibility": 1,
            "authorized": 1,
            "url": "http://cys.loe-seasons.local/promotion/1",
            "currency": "$",
            "featured": 0,
            "events_name" : ['ciberdays', 'travelsale'],
            "events_prefix" : ['cyl', 'tyl'],
            "categories_name" :  ['jueguetes', 'tecnologia'],
            "categories_id" : ['45', '78'],
            "sponsored_categories_name" : ['jasson brand', 'test brand'],
            "sponsored_categories_id" : ['78', '89'],
            "brand_id": 10,
            "brand_name": "jasson branc"
        }

        response = client.index_document(engine_name, document)
        print('Created docuemnt')
        print(response)


if __name__ == '__main__':
    Documents.create_document()
