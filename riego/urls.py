from django.urls import path, re_path
from django.conf.urls import include

from riego.views import riego_viewAll

urlpatterns = [
    re_path(r'^riego$', riego_viewAll.as_view()),
]