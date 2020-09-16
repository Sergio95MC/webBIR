from django.urls import path
from BIRQUIZ import views as BQviews

urlpatterns = [
    path('intro/', BQviews.intro),
]