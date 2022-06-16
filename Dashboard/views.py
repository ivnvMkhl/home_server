from django.shortcuts import render
from django.http import HttpResponse


def index(requiest):
    html = '<center><h1>My Home Server!</h1></center>'
    return HttpResponse(html)
