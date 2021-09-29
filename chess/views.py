from django.http import Http404
from django.http.response import JsonResponse
from django.views import View
from rest_framework import status
from .figure import PAWNS, COLUMNS, ROWS


def chessboard():
    chessboard_field = []
    for row in ROWS:
        for col in COLUMNS:
            chessboard_field.append(col + row)
    return chessboard_field


class AvailableMove(View):

    def get(self, request, chess_figure, current_field):
        try:
            figure = PAWNS[chess_figure](current_field)
            available_move = figure.list_available_moves()
            error = None
            _status = status.HTTP_200_OK
        except KeyError:
            raise Http404
        if current_field.upper() not in chessboard():
            available_move = []
            error = "Field does not exist."
            _status = status.HTTP_409_CONFLICT
        content = {
            "availableMoves": available_move,
            "figure": chess_figure,
            "error": error,
            "currentField": current_field.upper()
                    }
        return JsonResponse(data=content, status=_status)


class ValidateAvailableMove(View):

    def get(self, request, chess_figure, current_field, dest_field):
        try:
            figure = PAWNS[chess_figure](current_field)
            error = None
            _status = status.HTTP_200_OK
        except KeyError:
            raise Http404
        if current_field.upper() not in chessboard() or \
                dest_field.upper() not in chessboard():
            move = "invalid"
            error = "Field does not exist."
            _status = status.HTTP_409_CONFLICT
        else:
            if figure.validate_move(dest_field):
                move = "valid"
            else:
                move = "invalid"
                error = "Current move is not permitted."
                _status = status.HTTP_409_CONFLICT
        content = {
            "move": move,
            "error": error,
            "figure": chess_figure,
            "currentField": current_field.upper(),
            "destField": dest_field.upper()
                    }
        return JsonResponse(data=content, status=_status)


available_move = AvailableMove.as_view()
validate_available_move = ValidateAvailableMove.as_view()
