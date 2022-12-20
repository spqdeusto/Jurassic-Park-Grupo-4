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

        x = requests.get('http://localhost:8000/dinosaur/create')
        jsonResponse = x.json()[0]

        if (x.status_code == 200):
            assert x.status_code == 200
            print ("CREATE DINOSAUR TEST PASSED")

        if (x.status_code != 200):
            print ("CREATE DINOSAUR TEST NOT PASSED")
            print (x.status_code)  


if __name__ == '__main__':
    unittest.main()






#from typing import Union
#from app.controllers.handler import Controllers
#from app.mysql.mysql import DatabaseClient

#import app.utils.vars as gb
#import app.models.models as models

#class test(unittest.TestCase):

    #def create_dinosaur(self):
        #dinoTest = ["Test",1,20,20,"male","peaceful","1"]
        #Controllers.create_dinosaur(dinoTest)
        #dinosaurs = Controllers.get_dinosaurs(self)
        #self.assertTrue(dinoTest)
        