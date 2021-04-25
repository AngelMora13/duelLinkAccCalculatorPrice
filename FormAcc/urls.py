from django.urls import path
from . import views

app_name="calculator"
urlpatterns=[
    path("", views.FormCalc,name="FormCalc")
]
