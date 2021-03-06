from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name="post_new"),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('project', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    # path('login/$', auth_views.login, {'template_name': 'blog/login.html'}, name='login'),
    path("login/", auth_views.LoginView.as_view(template_name = "blog/login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout")
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)