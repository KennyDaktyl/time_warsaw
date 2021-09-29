from django.urls import path

from .views import available_move, validate_available_move

# CartDetails,
urlpatterns = [
    path('<slug:chess_figure>/<slug:current_field>', available_move, name="available_move"),
    path('<slug:chess_figure>/<slug:current_field>/<slug:dest_field>', validate_available_move, name="validate_available_move"),
]