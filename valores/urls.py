from django.urls import path, re_path
from django.conf.urls import include

from valores.views import valores_viewAll, valores_viewAmbiente, valores_viewSuelo, valores_viewAgua

urlpatterns = [
    re_path(r'^valores$', valores_viewAll.as_view()),
    re_path(r'^valores/ambiente$', valores_viewAmbiente.as_view()),
    re_path(r'^valores/suelo$', valores_viewSuelo.as_view()),
    re_path(r'^valores/agua$', valores_viewAgua.as_view()),
]