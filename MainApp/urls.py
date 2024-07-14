from django.urls import path
from  . import views


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('view-image/<str:pk>/', views.viewImg, name='view-image'),
    path('add-image/', views.addImg, name='add-image'),
]
