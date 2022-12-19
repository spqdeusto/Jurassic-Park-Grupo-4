import unittest

from typing import Union
from app.controllers.handler import Controllers
from app.mysql.mysql import DatabaseClient

import app.utils.vars as gb
import app.models.models as models

class test(unittest.TestCase):

    def create_dinosaur(self):
        dinoTest = ["Test",1,20,20,"male","peaceful","1"]
        Controllers.create_dinosaur(dinoTest)
        dinosaurs = Controllers.get_dinosaurs(self)
        self.assertTrue(dinoTest)
        