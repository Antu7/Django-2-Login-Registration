
# Login Urls


from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.loginView, name='loginView'),
    path('loginCheck', views.loginCheck, name = 'loginCheck'),
    path('registration', views.registration, name='registration'),
    path('home', views.home, name='home'),
    path('logout_view', views.logout_view, name="logout_view")
]
