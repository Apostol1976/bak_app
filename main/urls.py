

from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
   
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contakt/', views.contakt, name='contakt'),
    path('why/', views.why, name='why'),
    path('message/', views.message, name='message'),
    path('montaz/', views.montaz, name='montaz'),
    path('umdom/', views.umdom, name='umdom'),
    path('remont/', views.remont, name='remont'),
]
