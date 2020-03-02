import requests
from bs4 import BeautifulSoup as bs

from gist_kakao_api.models import CafeteriaMenu


def get_cafeteria1():
    cafeteria_m = CafeteriaMenu.objects.filter(cafeteria=1).last()
    return cafeteria_m


def get_cafeteria2():
    cafeteria_m = CafeteriaMenu.objects.filter(cafeteria=2).last()
    return cafeteria_m


