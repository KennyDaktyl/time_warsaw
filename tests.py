import requests
import json

from chess.figure import Bishop, Pawn

url_base = "http://localhost:8000/api/v1/"

class TestAPI:

    def test_connect_url1(self):
        url = url_base + "pawn/h3"
        resp = requests.get(url)
        assert resp.status_code == 200

    def test_connect_url2(self):
        url = url_base + "pawn/h3/h4"
        resp = requests.get(url)
        assert resp.status_code == 200

    def test_not_on_chessboard_409_url1(self):
        url = url_base + "pawn/h22"
        resp = requests.get(url)
        assert resp.status_code == 409

    def test_not_on_chessboard_409_url2(self):
        url = url_base + "pawn/h2/h22"
        resp = requests.get(url)
        assert resp.status_code == 409

    def test_not_on_dictionary_404_url1(self):
        url = url_base + "pawnXXX/h22"
        resp = requests.get(url)
        assert resp.status_code == 404

    def test_not_on_dictionary_404_url2(self):
        url = url_base + "pawnXXX/h22/h1"
        resp = requests.get(url)
        assert resp.status_code == 404

    def test_available_moves_1(self):
        url = url_base + "pawn/a1"
        pawn = Pawn('A1')
        resp = requests.get(url)
        resp_json = json.loads(resp.text)
        assert resp_json.get("availableMoves") == pawn.list_available_moves()
        assert resp_json.get("availableMoves") == ['A2']

    def test_available_moves_2(self):
        url = url_base + "bishop/f3"
        bishop = Bishop('F3')
        resp = requests.get(url)
        resp_json = json.loads(resp.text)
        assert resp_json.get("availableMoves") == [
            "G4",
            "H5",
            "E4",
            "D5",
            "C6",
            "B7",
            "A8",
            "G2",
            "H1",
            "E2",
            "D1",
        ]
        assert resp_json.get("error") is None
        assert resp_json.get("availableMoves") == bishop.list_available_moves()
