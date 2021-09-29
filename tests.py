import pytest
import requests
import json
from django.urls import reverse

DJANGO_SETTINGS_MODULE = 'time_warsaw.settings'
python_files = 'tests.py' 

class TestMove:
    def test_connect_url1(self):
        url = 'http://localhost:8000/api/v1/pawn/h3'
        resp = requests.get(url)
        assert resp.status_code == 200

    def test_connect_url2(self):
        url = 'http://localhost:8000/api/v1/pawn/h3/h4'
        resp = requests.get(url)
        assert resp.status_code == 200

    def test_not_on_chessboard_409_url1(self):
        url = 'http://localhost:8000/api/v1/pawn/h22'
        resp = requests.get(url)
        assert resp.status_code == 409
    
    def test_not_on_chessboard_409_url2(self):
        url = 'http://localhost:8000/api/v1/pawn/h2/h22'
        resp = requests.get(url)
        assert resp.status_code == 409

    def test_not_on_dictionary_404_url1(self):
        url = 'http://localhost:8000/api/v1/pawnXXX/h22'
        resp = requests.get(url)
        assert resp.status_code == 404

    def test_not_on_dictionary_404_url2(self):
        url = 'http://localhost:8000/api/v1/pawnXXX/h22/h1'
        resp = requests.get(url)
        assert resp.status_code == 404
    
    def test_available_moves_1(self):
        url = 'http://localhost:8000/api/v1/pawn/a1'
        resp =  requests.get(url)
        resp_json = json.loads(resp.text)
        assert resp_json.get("availableMoves") == ["A2"]
    
    def test_available_moves_2(self):
        url = 'http://localhost:8000/api/v1/bishop/f3'
        resp =  requests.get(url)
        resp_json = json.loads(resp.text)
        assert resp_json.get("availableMoves") == ["G4", "H5", "E4", "D5", "C6", "B7", "A8", "G2", "H1", "E2", "D1"]
        assert resp_json.get("error") == None