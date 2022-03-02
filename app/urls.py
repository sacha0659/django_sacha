from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.edit, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('delete/<int:id>/', views.delete, name='delete'),
    
]