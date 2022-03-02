from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('/add/', views.edit, name='add'),
    path('/edit/(?P<id>\d+)/', views.edit, name='edit'),
    path('/delete/(?P<id>\d+)/', views.delete, name='delete'),
    # path(r'^members/detail/(?P<id>\d+)/$', views.detail, name='detail'),
]