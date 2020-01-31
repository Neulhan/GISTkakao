from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
