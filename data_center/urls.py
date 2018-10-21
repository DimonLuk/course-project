from django.conf.urls import url
from django.urls import include
from .views import test


urlpatterns = [
    url(r'^api/test', test)
]
