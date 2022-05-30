# from django.urls import re_path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.gallery,name = 'gallery'),
    url(r'^image/',views.display_image,name='displayImages'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^photo/(\d+)',views.image,name ='image'),
    ] 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)