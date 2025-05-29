from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("brands/", views.brand, name="brand"),
    path("categories/", views.product_category, name="product_category"),
    path("products/", views.product, name="product"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("blogs/", views.blog, name="blog"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("contact/", views.contact, name="contact"),
]