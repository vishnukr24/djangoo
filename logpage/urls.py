from django.urls import path
from .import views
urlpatterns = [
    path('home', views.register,name='home'),
    path('login', views.signin,name='signin'),
    path('',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('viewall',views.viewall,name='viewall'),
    path('upadatereg/<str:pk>/',views.updatereg,name='updatereg'),
    ]