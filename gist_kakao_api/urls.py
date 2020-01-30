from django.urls import path

from gist_kakao_api import views

urlpatterns = [
    path('', views.home),
    path('drf-test-get', views.drf_test_get),
    path('drf-test-post', views.drf_test_post),
]