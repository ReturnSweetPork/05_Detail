from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

app_name = "details"

urlpatterns = [
    path("", views.list),
    path("signup/", views.signup),
    path("mypage/", views.mypage),
    path("qna/", views.qna),
    path("<str:not_found>/", views.page),
    ]
    
