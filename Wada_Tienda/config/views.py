from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
	return HttpResponse("<br><br> Ya entendimos esto, es muy simple ;) ")

def index(request):
    return render(request, "index.html")

