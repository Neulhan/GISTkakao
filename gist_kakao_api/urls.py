from django.urls import path

from gist_kakao_api import views

urlpatterns = [
    path('', views.home),
    path('/', views.home2),
    # path('drf-test-get', views.drf_test_get),
    path('drf-test-post', views.drf_test_post),
    path('drf-diet', views.drf_diet),
    path('drf-schedule', views.drf_schedule),
    path('drf-weather', views.drf_weather),
]