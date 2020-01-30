from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


def home(request):
    return render(request, 'home.html')


@api_view(['GET'])
def drf_test_get(request):
    if request.method == 'GET':
        text = 'get success'
        version = '2.0'

        return Response({'version': version, 'template': {'outputs': [{'simpleText': {'text': text}}]}})


@api_view(['POST'])
def drf_test_post(request):
    if request.method == 'POST':
        text = 'post success'
        version = '2.0'

        return Response({'version': version, 'template': {'outputs': [{'simpleText': {'text': text}}]}})
