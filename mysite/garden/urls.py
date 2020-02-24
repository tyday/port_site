from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from garden import views

# urlpatterns = [
#     path('readings/', views.SensorReadingList.as_view()),
#     path('readings/<int:pk>/', views.SensorReadingDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'readings', views.SensorReadingViewSet, basename='reading')
urlpatterns = router.urls

urlpatterns.append(path('readingslist/', views.SensorReadingList.as_view()))