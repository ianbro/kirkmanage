from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('heart:dashboard'))),
    url(r'^helm/', admin.site.urls),
    url(r'^profile/', include("heart.urls", namespace="heart")),
    url(r'^budget/', include("budget.urls", namespace="budget")),
]
