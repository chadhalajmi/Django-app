from django.urls import path
from django.conf.urls import url
from blog import views
urlpatterns = [
    path("",views.Post,name='blog'),
    path('ajouter_Post/', views.addpost, name='ajouter_Post'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('register',views.register, name='register')

] 