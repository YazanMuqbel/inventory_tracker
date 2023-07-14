from django.urls import path     
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('sign_up/', views.sign_up, name='sign_up_page'),
    path('sign_in/', views.sign_in, name='sign_in_page'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_dashboard/', views.dashboard, name='user_dashboard'),
    path('control_panel/', views.control_panel, name= 'control_panel'),

]
