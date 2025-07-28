from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('destroy/<int:pk>', views.delete, name='destroy'),
]
