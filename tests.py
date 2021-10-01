import requests
import json

from chess.figure import Bishop, King, Knight, Pawn, Queen, Rook

url_base = "http://localhost:8000/api/v1/"


def respone(figure, url_full, param_1, param_2, param_3_failed,
            available_move_list=False):
    resp = requests.get(url_full + param_1)
    resp_json = json.loads(resp.text)
    assert resp_json.get("availableMoves") == figure.list_available_moves()
    if available_move_list:
        assert resp_json.get("availableMoves") == available_move_list
    else:
        assert resp_json.get("availableMoves") == [param_2]
    resp = requests.get(url_full + param_1 + "/" + param_2)
    resp_json = json.loads(resp.text)
    assert resp_json.get("move") == "valid"
    url = url_full + param_1 + "/" + param_3_failed
    resp = requests.get(url)
    resp_json = json.loads(resp.text)
    assert resp_json.get("move") == "invalid"


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

    def test_available_moves_pawn(self):
        figure = "pawn"
        param_1 = "A1"
        param_2 = "A2"
        param_3_failed = "A3"
        url_full = url_base + figure + "/"
        figure = Pawn("A1")

        respone(figure, url_full, param_1, param_2, param_3_failed)

    def test_available_move_rook(self):
        available_move = [
            "G5",
            "H6",
            "E5",
            "D6",
            "C7",
            "B8",
            "G3",
            "H2",
            "E3",
            "D2",
            "C1",
        ]
        figure = "rook"
        param_1 = "F4"
        param_2 = "F8"
        param_3_failed = "A3"
        url_full = url_base + figure + "/"
        figure = Rook(param_1)
        respone(
            figure, url_full, param_1, param_2, param_3_failed, available_move)

    def test_available_moves_bishop(self):
        available_move = [
            "F5",
            "F6",
            "F7",
            "F8",
            "F1",
            "F2",
            "F3",
            "G4",
            "H4",
            "A4",
            "B4",
            "C4",
            "D4",
            "E4",
        ]
        figure = "bishop"
        param_1 = "F4"
        param_2 = "F8"
        param_3_failed = "A3"
        url_full = url_base + figure + "/"
        figure = Bishop(param_1)
        respone(
            figure, url_full, param_1, param_2, param_3_failed, available_move)

    def test_available_move_knight(self):
        available_move = ["G6", "E6", "G2", "E2", "H5", "D5", "H3", "D3"]
        figure = "knight"
        param_1 = "F4"
        param_2 = "G2"
        param_3_failed = "A3"
        url_full = url_base + figure + "/"
        figure = Knight(param_1)
        respone(
            figure, url_full, param_1, param_2, param_3_failed, available_move)

    def test_available_move_queen(self):
        available_move = [
            "A2",
            "A3",
            "A4",
            "A5",
            "A6",
            "A7",
            "A8",
            "B1",
            "C1",
            "D1",
            "E1",
            "F1",
            "G1",
            "H1",
            "B2",
            "C3",
            "D4",
            "E5",
            "F6",
            "G7",
            "H8",
        ]
        figure = "queen"
        param_1 = "A1"
        param_2 = "A5"
        param_3_failed = "G2"
        url_full = url_base + figure + "/"
        figure = Queen(param_1)
        respone(
            figure, url_full, param_1, param_2, param_3_failed, available_move)

    def test_available_move_king(self):
        available_move = ["G4", "G3", "G2", "F2", "E2", "E3", "E4", "F4"]
        figure = "king"
        param_1 = "F3"
        param_2 = "F4"
        param_3_failed = "A1"
        url_full = url_base + figure + "/"
        figure = King(param_1)
        respone(
            figure, url_full, param_1, param_2, param_3_failed, available_move)
