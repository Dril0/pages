from django.urls import path
from .views import HomePageView, AboutPageView  # importamos desde app/views.

"""usando class based views siempre se agrega el as_view al final del viewname"""
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
