from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("services/", views.service, name="service"),
    path("blogs/", views.blog, name="blog"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("contact/", views.contact, name="contact"),
]