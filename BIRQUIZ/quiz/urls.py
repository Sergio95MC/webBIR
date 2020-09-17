from django.urls import path
from . import views

urlpatterns = [
    path('intro/', views.intro, name = "inicio"),
    path('instrucciones/', views.instrucciones, name = "instrucciones"),
    path('QUIZ/', views.QUIZ, name = "quiz"),
    path('CONTACTO/', views.contacto, name = "contacto"),

]