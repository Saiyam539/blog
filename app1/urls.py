from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='home'),
    path('about',about,name='about'),
    path('post',post,name='post'),
    path('view_post/<int:id>/',view_post,name='view_post')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
