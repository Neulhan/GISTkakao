from django.db import models
import os
from uuid import uuid4
from django.utils import timezone


def date_upload_to(instance, filename):
    # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    # 길이 32 인 uuid 값
    uuid_name = uuid4().hex
    # 확장자 추출
    extension = os.path.splitext(filename)[-1].lower()
    # 결합 후 return
    return '/'.join([
        ymd_path,
        uuid_name + extension,
        ])


class CafeteriaMenu(models.Model):
    post_url = models.URLField(default='www.lawandgood.com')
    cafeteria = models.IntegerField(default=1)
    title = models.CharField(max_length=255)
    menu_img = models.URLField()


class Schedule(models.Model):
    when = models.CharField(max_length=255)
    text = models.TextField()