import requests
from bs4 import BeautifulSoup as bs
import datetime
from urllib import parse

from django.utils import timezone

time_mapping = {
    '0': '23',
    '1': '23',
    '2': '02',
    '3': '02',
    '4': '02',
    '5': '05',
    '6': '05',
    '7': '05',
    '8': '08',
    '9': '08',
    '10': '08',
    '11': '11',
    '12': '11',
    '13': '11',
    '14': '14',
    '15': '14',
    '16': '14',
    '17': '17',
    '18': '17',
    '19': '19',
    '20': '20',
    '21': '20',
    '22': '22',
    '23': '23',
    '24': '23',
}

data_mapping = {
    'POP': '강수확률',
    'PTY': '강수형태',
    'R06': '6시간 강수량',
    'REH': '습도',
    'S06': '6시간 신적설',
    'SKY': '하늘상태',
    'T3H': '3시간 기온',
    'UUU': '풍속(동서)',
    'VEC': '풍향',
    'VVV': '풍속(남북)',
    'WSD': '풍속',
    'WAV': '파고',
    'TMX': '낮 최고기온',
    'TMN': '아침 최저기온',
    'T1H': '기온',
    'RN1': '1시간 강수량'
}


def getVilageFcst():
    base_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
    key = 'D6vdl5myJ0a0xl%2FDzf61U3kriBw%2FiCmMqJoIAoJ3Mg4kFkmXD1Wj6WwehGkJFW%2FIXJ4hd6l%2BAlVrB4DXKlsL2w%3D%3D'

    now = timezone.now()

    if str(now.hour) == "0" or "1":
        delta = datetime.timedelta(hours=1)
        now = now - delta

    date_now = now.strftime("%Y%m%d")
    params = f"serviceKey={key}&numOfRows=10&pageNo=1&base_time={time_mapping[str(now.hour)]}00&base_date={date_now}&nx=58&ny=76"
    query = parse.parse_qs(params)
    url = base_url+"?"+parse.urlencode(query, doseq=True)

    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    result_data = {}
    for i in soup.select('item'):
        result_data[data_mapping[i.select_one('category').text]] = i.select_one('fcstvalue').text

    return result_data


def getUltraSrtNcst():
    base_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
    key = 'D6vdl5myJ0a0xl%2FDzf61U3kriBw%2FiCmMqJoIAoJ3Mg4kFkmXD1Wj6WwehGkJFW%2FIXJ4hd6l%2BAlVrB4DXKlsL2w%3D%3D'

    now = timezone.now()

    if str(now.hour) == "0" or "1":
        delta = datetime.timedelta(hours=1)
        now = now - delta

    date_now = now.strftime("%Y%m%d")
    params = f"serviceKey={key}&numOfRows=10&pageNo=1&base_time={time_mapping[str(now.hour)]}00&base_date={date_now}&nx=58&ny=76"
    query = parse.parse_qs(params)
    url = base_url + "?" + parse.urlencode(query, doseq=True)
    print(url)
    html = requests.get(url).text
    soup = bs(html, 'html.parser')

    result_data = {}
    for i in soup.select('item'):
        result_data[data_mapping[i.select_one('category').text]] = i.select_one('obsrvalue').text

    return result_data

