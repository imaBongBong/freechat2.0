from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('create_room/',views.create_room,name='create_room'),
    path('delete_room/<str:pk>/',views.delete_room,name='delete_room'),
    path('edit_room/<str:pk>/',views.edit_room,name='edit_room'),
    path('single_room/<str:pk>/',views.single_room,name='single_room'),
    path('activity/',views.activity_page,name='activity'),
    path('topics/',views.topics_page,name='topics'),
]