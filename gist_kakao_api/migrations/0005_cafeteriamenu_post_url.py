# Generated by Django 2.1 on 2020-02-16 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gist_kakao_api', '0004_cafeteriamenu_cafeteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafeteriamenu',
            name='post_url',
            field=models.URLField(default='www.lawandgood.com'),
        ),
    ]
