import requests
from bs4 import BeautifulSoup as bs


html = requests.get('https://www.gist.ac.kr/kr/html/sub05/0501.html').text
soup = bs(html, 'html.parser')
obj = []
# '#au_board_list:first-child > .title > a'
kk = 1
ulul=soup.select('.schtxt>ul')
for i in ulul:
    print(str(kk)+"월")
    kk = kk+1
    for iq in i.select('li'):
        print(iq.text)

