from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/', views.cat_list, name='cat_list'),
    path('cats/create/', views.create_cat, name='create_cat'),
    path('cats/edit/<int:cat_id>/', views.edit_cat, name='edit_cat'),
    path('cats/delete/<int:cat_id>/', views.delete_cat, name='delete_cat'),
    path('cats/play/<int:cat_id>/', views.play_cat, name='play_cat'),
    path('rating/', views.rating, name='rating'),

]
