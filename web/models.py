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


class ProductCategory(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('web:product_category_detail', kwargs={'slug': self.slug})

    def get_products(self):
        return Product.objects.filter(category=self)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey("web.Brand", on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    title = models.CharField(max_length=180)
    slug = models.SlugField()
    image = models.ImageField(upload_to="product/")
    description = HTMLField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('web:product_detail', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductEnquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=180)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Enquiry"
        verbose_name_plural = "Product Enquiries"

    
class Brand(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to="brand/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class FAQ(models.Model):
    question = models.CharField(max_length=180)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"