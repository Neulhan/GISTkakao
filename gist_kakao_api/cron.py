import requests
from bs4 import BeautifulSoup as bs

from gist_kakao_api.models import CafeteriaMenu


def get_cafeteria_2_crawling():
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
    detail_soup = bs(requests.get(detail_url).text, 'html.parser')
    title = detail_soup.select_one('.bd_detail_tit h2').text
    img_src = detail_soup.select_one('.bd_detail_content img').get('src')

    cafeteria_m = CafeteriaMenu.objects.create(menu_img=img_src, title=title, cafeteria=2, post_url=detail_url)

    return 0


def get_cafeteria_1_crawling():
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
    return 0
