from . import views
from django.urls import path
urlpatterns = [
    path("index/", views.hello, name="greet"),
    path("hello/", views.say_hello, name="hello"),
    path("more/", views.more_html, name = "more")
]