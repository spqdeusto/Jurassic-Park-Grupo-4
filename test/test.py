import unittest
import requests
import json

class testCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_dinosaur(self):
        url = 'http://localhost:8000/dinosaur/create'
        myobj = {
            "name": "dinosaurX",
            "specie-id": 8,
            "age": 20,
            "weight": 60,
            "gender": "male",
            "dangerousness": "peaceful",
            "enclosure_id": 1
        }
        x = requests.post(url, json = myobj)

        x = requests.get('http://localhost:8000/dinosaur/get_all')
        jsonResponse = x.json()
        last = jsonResponse[len(jsonResponse)-1]

        self.assertTrue(last['name'] == 'dinosaurX')

    def test_create_specie(self):
        url = 'http://localhost:8000/specie/create'
        myobj = {
            "name": "specieX"
        }
        x = requests.post(url, json = myobj)

        x = requests.get('http://localhost:8000/specie/get_all')
        jsonResponse = x.json()
        last = jsonResponse[len(jsonResponse)-1]

        self.assertTrue(last['name'] == 'specieX')

    def test_create_enclosure(self):
        url = 'http://localhost:8000/enclosure/create'
        myobj = {
            "name": "enclosureX",
            "status": True
        }
        x = requests.post(url, json = myobj)

        x = requests.get('http://localhost:8000/enclosure/get_all')
        jsonResponse = x.json()
        last = jsonResponse[len(jsonResponse)-1]

        self.assertTrue(last['name'] == 'enclosureX')


    def test_create_offroad(self):
        x = requests.get('http://localhost:8000/offroad/get_all')
        jsonResponse = x.json()
        firstLen = len(jsonResponse)

        url = 'http://localhost:8000/offroad/create'
        myobj = {
            "on_route": True,
            "n_visitors": 1,
            "security_system": False
        }
        x = requests.post(url, json = myobj)

        x = requests.get('http://localhost:8000/offroad/get_all')
        jsonResponse = x.json()
        secondLen = len(jsonResponse)

        self.assertTrue(firstLen+1 == secondLen)

if __name__ == '__main__':
    unittest.main()