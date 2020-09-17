from django.http import HttpResponse
import datetime, os
from django.template import Template, Context
#from pathlib import Path
from django.template import loader
from django.shortcuts import render


def intro(request):

    fecha_actual = datetime.datetime.now().date
    return render(request, 'intro.html', {'dameFecha':fecha_actual})
  



def instrucciones(request):

    return render(request, 'instrucciones.html')


def QUIZ(request):

    return render(request, 'quiz.html')

def contacto(request):

    return render(request, 'contacto.html')

