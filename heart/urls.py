from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login

from heart.views import dashboard

urlpatterns = [
    url(r'^dashboard', dashboard, name="dashboard"),
    url(r'^login', login, name="login"),
]
