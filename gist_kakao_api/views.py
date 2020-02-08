from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    return Response('zappa-gist-success')


@api_view(['GET'])
def home2(request):
    return Response('zappa-gist-success2')


@api_view(['POST'])
def drf_test_post(request):
    if request.method == 'POST':
        version = '2.0'
        card_list = []

        simple_text = {
            "simpleText": {
                "text": "간단한 텍스트 요소입니다."
            }
        }
        treasure = {
            "commerceCard": {
                "description": "따끈따끈한 보물 상자 팝니다",
                "price": 10000,
                "discount": 1000,
                "currency": "won",
                "thumbnails": [
                    {
                        "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
                        "link": {
                            "web": "https://store.kakaofriends.com/kr/products/1542"
                        }
                    }
                ],
                "profile": {
                    "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                    "nickname": "보물상자 팝니다"
                },
                "buttons": [
                    {
                        "label": "구매하기",
                        "action": "webLink",
                        "webLinkUrl": "https://store.kakaofriends.com/kr/products/1542"
                    },
                    {
                        "label": "전화하기",
                        "action": "phone",
                        "phoneNumber": "354-86-00070"
                    },
                    {
                        "label": "공유하기",
                        "action": "share"
                    }
                ]
            }
        }

        card_list.append(simple_text)
        card_list.append(treasure)

        context = {
            'version': version,
            'template': {
                'outputs': card_list
            }
        }
        return Response(context)


@api_view(['POST'])
def drf_weather(request):
    if request.method == 'POST':
        version = '2.0'
        card_list = []
        simple_text = {
            "simpleText": {
                "text": "날씨 API 호출"
            }
        }
        card_list.append(simple_text)

        context = {
            'version': version,
            'template': {
                'outputs': card_list
            }
        }
        return Response(context)


@api_view(['POST'])
def drf_schedule(request):
    if request.method == 'POST':
        version = '2.0'
        card_list = []
        simple_text = {
            "simpleText": {
                "text": "학사일정 API 호출"
            }
        }
        card_list.append(simple_text)

        context = {
            'version': version,
            'template': {
                'outputs': card_list
            }
        }
        return Response(context)


@api_view(['POST'])
def drf_diet(request):
    if request.method == 'POST':
        version = '2.0'
        card_list = []
        simple_text = {
            "simpleText": {
                "text": "학식 API 호출"
            }
        }
        card_list.append(simple_text)

        context = {
            'version': version,
            'template': {
                'outputs': card_list
            }
        }

        return Response(context)


@api_view(['POST'])
def test(request):
    params = request.data['action']['detailParams']

    korean = int(params['점수']['origin'])
    math = int(params['점수1']['origin'])
    english = int(params['점수2']['origin'])
    science1 = int(params['점수3']['origin'])
    science2 = int(params['점수4']['origin'])
    version = '2.0'

    card_list = []
    simple_text = {
        "simpleText": {
            "text": f"""
            국어: {korean}
            수학: {math}
            영어: {english}
            탐구1: {science1}
            탐구2: {science2}
            총합: {korean+math+english+science1+science2})
            합격여부: 합격
            """
        }
    }
    card_list.append(simple_text)

    context = {
        'version': version,
        'template': {
            'outputs': card_list
        }
    }
    return Response(context)
