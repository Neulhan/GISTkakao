#   패키지 정보 업데이트 ...
sudo -H apt-get -y update

#   build essential 설치
sudo -H apt-get  -y build-essential

# 파이썬 깔기
sudo -H apt-get  -y install python3

# pip 깔기
sudo -H apt-get  -y install python3-pip

# pip 업그레이드
sudo -H pip3 install --upgrade pip

#  가상환경깔기
sudo apt-get  -y install virtualenv

#    uwsgi 깔기
pip install uwsgi

#    nginx 깔기
sudo apt-get install nginx
