from django.urls import path

from . import views

urlpatterns = [
    path('', views.weather, name='weather'),
    path('weather/<int:pk>/', views.observation_detail, name='observation_detail'),
    path('weather/new/', views.observation_new, name='observation_new'),
    path('observations/', views.ObservationList.as_view()),
    path('observation/<int:pk>/edit/', views.observation_edit, name='observation_edit'),
    path('plot/', views.plot, name='plot')
]