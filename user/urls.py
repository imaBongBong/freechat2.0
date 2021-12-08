from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('register/',views.user_register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/<str:pk>/',views.user_profile,name='profile'),
    path('update_profile',views.update_profile,name='update_profile'),
]