from django.urls import path
from . import views

urlpatterns = [
    path('all_recipe/', views.all_recipe, name='all_recipe'),  
    path('view_recipe/', views.view_recipe, name='view_recipe'),  
    path('my_recipe/', views.my_recipe, name='my_recipe'),  
    path('create_my_recipe/', views.create_my_recipe, name='create_my_recipe'),  
    path('edit_my_recipe/', views.edit_my_recipe, name='edit_my_recipe'),  
    path('delete_my_recipe/', views.delete_my_recipe, name='delete_my_recipe'),  
]