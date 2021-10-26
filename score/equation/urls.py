from django.urls import path
from .views import exercise, judge, login, wrong_notebook

urlpatterns = [
    path('', login),
    path('exercise/<str:account>/', exercise),
    path('judge/<str:account>/<str:question>/<str:right_answer>', judge, name="judge"),
    path("notebook/<str:account>/", wrong_notebook),
]
