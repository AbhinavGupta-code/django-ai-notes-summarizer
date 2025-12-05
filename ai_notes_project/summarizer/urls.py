from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
]
