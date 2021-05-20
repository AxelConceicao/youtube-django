from django.urls import path
from . import views

app_name = "video"
urlpatterns = [
    path('video/upload', views.upload, name='upload'),
    path('video/upload/thumbnail', views.save_thumbnail, name='save_thumbnail'),
    path('video/watch/<str:id>/', views.watch, name='watch'),
    path('video/watch/<str:id>/like/', views.like, name='like'),
    path('video/watch/<str:id>/dislike/', views.dislike, name='dislike'),
    path('video/watch/', views.watch, name='watch'),
    path('video/channel/<str:username>', views.channel, name='channel'),
    path('video/channel/<str:username>/subscribe', views.subscribe, name='subscribe'),
    path('video/channel/<str:username>/unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('', views.index, name='index'),
]