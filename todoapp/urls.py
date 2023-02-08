
from django.urls import path,include
from.import views

urlpatterns = [
    path('', views.home,name='home'),
    path('createpost', views.createpost,name='createpost'),
    path('deletepost/<str:pk>/', views.deletepost,name='deletepost'),
    path('updatepost/<str:pk>/', views.updatepost,name='updatepost'),
]