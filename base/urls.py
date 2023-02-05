from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
  
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),

    path('create_room/', views.createRoom, name='create-room'),
    path('update_room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete_room/<str:pk>', views.deleteRoom, name='delete-room'),
]
