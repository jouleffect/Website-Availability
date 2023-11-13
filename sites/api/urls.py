from django.urls import path
from . import views

urlpatterns = [
    path("sites/", views.IndexView.as_view(), name="index"),
    path("sites/u=<path:url>/r=<path:regex>", views.UrlRegexAPIView.as_view(), name="url&regex") ,
    path("sites/u=<path:url>/", views.UrlAPIView.as_view(), name="url")       
]