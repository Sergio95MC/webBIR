from django.urls import path
from . import views

urlpatterns = [
    path('intro/', views.intro, name = "página de inicio"),

]