from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login_base, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_base, name='logout'),    
]