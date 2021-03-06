from django.urls import include, path
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r'observations', views.ObservationViewSet)

urlpatterns = [
    path('', views.weather, name='weather'),
    path('weather/<int:pk>/', views.observation_detail, name='observation_detail'),
    path('weather/new/', views.observation_new, name='observation_new'),
    path('observations/', views.ObservationList.as_view()),
    path('observation/<int:pk>/edit/', views.observation_edit, name='observation_edit'),
    path('plot/', views.plot, name='plot'),
    path('api/', include(router.urls)),
    path('findcity/', views.find_city_req, name='find_city')

]