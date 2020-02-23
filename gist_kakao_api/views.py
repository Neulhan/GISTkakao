from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from gist_kakao_api.dietAPI import get_cafeteria1, get_cafeteria2
from gist_kakao_api.models import CafeteriaMenu
from gist_kakao_api.weatherAPI import *

API_END_POINT = 'https://m14fvnt238.execute-api.ap-northeast-2.amazonaws.com/dev10'


def test_img(request):
    context = {'cafe': CafeteriaMenu.objects.all()}
    return render(request, 'home.html', context)


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
        weather_data = getUltraSrtNcst()
        weather_data.update(getVilageFcst())
        print(weather_data)
        a = {'강수형태': '0', '습도': '70', '1시간 강수량': '0', '기온': '10',
             '풍속(동서)': '0.6', '풍향': '270', '풍속(남북)': '0', '풍속': '0.6',
             '강수확률': '0', '하늘상태': '1', '3시간 기온': '3'}

        try:
            text = f"오늘의 GIST 날씨\n 기온 : {weather_data['기온']}\n습도 : {weather_data['습도']}"
        except KeyError as e:
            print(KeyError)
            text = f"오늘의 GIST 날씨\n 기온 : {weather_data['3시간 기온']}\n습도 : {weather_data['습도']}"

        if weather_data['강수형태'] == '1':
            rain_text = f"\n현재날씨 : 비"
        else:
            rain_text = f"\n강수확률 : {weather_data['강수확률']}"
        text += rain_text
        simple_text = {
                "simpleText": {
                    "text": text
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
                "text": "2월 학사일정\n12-23(월) ~ 02-28(금)동계방학\n02-03(월) ~ 02-07(금)1학기 전과지원서 제출\n02-07(금)겨울학기 성적 제출마감\n02-14(금)2019학년도 학위수여식\n02-17(월) ~ 02-26(수)GIST대학 신입생 오리엔테이션\n02-17(월) ~ 02-21(금)2020학년도 1학기 수강신청, 복학원 제출 및 등록\n02-24(월)2020학년도 1학기 대학원 신입생 오리엔테이션\n02-24(월) ~ 02-25(화)2020학년도 1학기 대학원 신입생 수강신청\n02-24(월) ~ 02-25(화)2020학년도 1학기 GIST대학 신입생 수강신청\n02-26(수)입학식"
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
def drf_diet_1(request):
    if request.method == 'POST':
        print('diet api call ->')
        cafe1 = get_cafeteria1()
        version = '2.0'
        card_list = []
        simple_image1 = {
            "simpleImage": {
                "imageUrl": cafe1.menu_img,
                "altText": cafe1.title
            }
        }

        card_list.append(simple_image1)

        context = {
            'version': version,
            'template': {
                'outputs': card_list
            }
        }

        print(context)
        return Response(context)


@api_view(['POST'])
def drf_diet_2(request):
    if request.method == 'POST':
        print('diet api call ->')
        cafe1 = get_cafeteria2()
        version = '2.0'
        card_list = []
        simple_image2 = {
            "simpleImage": {
                "imageUrl": cafe1.menu_img,
                "altText": cafe1.title
            }
        }
        card_list.append(simple_image2)

        context = {
            'version': version,
            'template': {
                'outputs': card_list
            }
        }
        print(context)
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


@api_view(['POST'])
def get_cafeteria_2_crawling(request):
    cafeteria2 = 'https://www.gist.ac.kr/kr/html/sub05/050602.html'
    html = requests.get(cafeteria2).text
    soup = bs(html, 'html.parser')
    a_list = soup.select('.bd_list_wrap .bd_item_box a')
    detail_url = cafeteria2 + a_list[0].get('href')

    try:
        cafeteria_m = CafeteriaMenu.objects.get(post_url=detail_url)
        return cafeteria_m

    except Exception:
        pass
    print("까꿍", detail_url)
    detail_soup = bs(requests.get(detail_url).text, 'html.parser')
    title = detail_soup.select_one('.bd_detail_tit h2').text
    img_src = detail_soup.select_one('.bd_detail_content img').get('src')

    cafeteria_m = CafeteriaMenu.objects.create(menu_img=img_src, title=title, cafeteria=2, post_url=detail_url)

    return Response(200)


@api_view(['POST'])
def get_cafeteria_1_crawling(request):
    cafeteria1 = 'https://www.gist.ac.kr/kr/html/sub05/050601.html'
    html = requests.get(cafeteria1).text
    soup = bs(html, 'html.parser')
    a_list = soup.select('.bd_list_wrap .bd_item_box a')
    detail_url = cafeteria1 + a_list[0].get('href')

    try:
        cafeteria_m = CafeteriaMenu.objects.get(post_url=detail_url)
        return cafeteria_m

    except Exception:
        pass
    detail_soup = bs(requests.get(detail_url).text, 'html.parser')
    title = detail_soup.select_one('.bd_detail_tit h2').text
    img_src = detail_soup.select_one('.bd_detail_content img').get('src')

    cafeteria_m = CafeteriaMenu.objects.create(menu_img=img_src, title=title, cafeteria=1, post_url=detail_url)
    return Response(200)