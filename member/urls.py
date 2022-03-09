from unicodedata import name
from django.urls import path
from .views import Home, Incity, Ininterest

urlpatterns = [
    path('', Home.as_view(), name="member.home"),
    path('<int:id>/incity/', Incity.as_view(), name="member.incity"),
    path('<int:id>/ininterest/', Ininterest.as_view(), name="member.ininterest"),
]
