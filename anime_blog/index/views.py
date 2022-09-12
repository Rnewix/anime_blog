from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
async def index(request):
    return HttpResponse('holachon')