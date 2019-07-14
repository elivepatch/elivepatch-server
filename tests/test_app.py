from elivepatch_server import app as flask_app
import pytest
from flask_restful import Api as api
from conftest import app
import unittest


class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = flask_app.test_client()

    def test_not_found(self):
        response = self.app.get("/")
        assert response.status_code == 404

    def test_found(self):
        response = self.app.get("/elivepatch/api/")
        assert response.status_code == 200
