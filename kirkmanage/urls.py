from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^helm/', admin.site.urls),
    url(r'^budget/', include("budget.urls", namespace="budget")),
]
