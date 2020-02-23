from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from gist_kakao_api import views

urlpatterns = [
    path('', views.home),
    path('/', views.home2),
    # path('drf-test-get', views.drf_test_get),
    path('drf-test-post', views.drf_test_post),
    path('drf-diet/1/', views.drf_diet_1),
    path('drf-diet/2/', views.drf_diet_2),
    path('drf-schedule', views.drf_schedule),
    path('drf-weather', views.drf_weather),
    path('test', views.test),
    path('get_cafeteria_1_crawling', views.get_cafeteria_1_crawling),
    path('get_cafeteria_2_crawling', views.get_cafeteria_2_crawling)

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
