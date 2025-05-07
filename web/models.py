from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse_lazy

class Banner(models.Model):
    title = models.CharField(max_length=180)
    sub_title = models.CharField(max_length=180)
    image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    
class Contact(models.Model):
    name = models.CharField(max_length=180)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=180)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    
class Blog(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField()
    date = models.DateField()
    image = models.ImageField(upload_to="blog/")
    description = HTMLField()

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse_lazy('web:blog_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"