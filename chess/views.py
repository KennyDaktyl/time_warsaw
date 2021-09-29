from django import views
from django.http import JsonResponse, Http404
from django.views import View

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
        except:
            raise Http404
        if current_field.upper() not in chessboard():
            available_move = []
            error = "Field does not exist."
        return JsonResponse({
            "availableMoves": available_move,
            "error": error,
            "figure": chess_figure,
            "currentField": current_field
                    })

class ValidateAvailableMove(View):

    def get(self, request, chess_figure, current_field, dest_field):
        return JsonResponse({})

available_move = AvailableMove.as_view()
validate_available_move = ValidateAvailableMove.as_view()