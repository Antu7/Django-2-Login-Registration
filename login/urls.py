# Login Urls


from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.loginView, name='loginView'),
    path('loginCheck', views.loginCheck, name='loginCheck'),
    path('registration', views.registration, name='registration'),
    path('home', views.home, name='home'),
    path('admin', views.admin, name='admin'),
    path('editUserInfo', views.editUserInfo, name='editUserInfo'),
    path('addReport', views.addReport, name='addReport'),
    path('addReportInformation', views.addReportInformation, name='addReportInformation'),
    path('viewAllReport/<int:id>/', views.viewAllReport, name='viewAllReport'),
    path('editReportInfo/<int:id>/', views.editReportInfo, name='editReportInfo'),
    path('deleteReportInfo/<int:id>/', views.deleteReportInfo, name='deleteReportInfo'),
    path('UpdateReportInfo', views.UpdateReportInfo, name='UpdateReportInfo'),
    path('updateUserInfo', views.updateUserInfo, name='updateUserInfo'),
    path('logout_view', views.logout_view, name="logout_view"),

    path('testPrint', views.testPrint, name="testPrint"),
    # url(r'^testPrint/$', testPrint.as_view()),
]


