import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.db.models import Count

from .models import Banner, Blog, Product, Brand, FAQ, ProductCategory, Meta
from .forms import ContactForm, ProductEnquiryForm


def index(request):
    banners = Banner.objects.all()
    blogs = Blog.objects.all()[:3]
    product_categories = ProductCategory.objects.all()
    faqs = FAQ.objects.all()
    brands = Brand.objects.all()
    meta = Meta.objects.filter(page="home").first()
    context = {"is_index": True, "banners":banners, "blogs":blogs, "product_categories":product_categories, "faqs":faqs, "brands":brands, "meta":meta}
    return render(request, "web/index.html", context)


def about(request):
    meta = Meta.objects.filter(page="about").first()
    context = {
        "is_about": True,
        "meta":meta
    }
    return render(request, "web/about.html", context)


def brand(request):
    meta = Meta.objects.filter(page="brands").first()
    brands = Brand.objects.all()

    context = {
        "is_brands":True,
        "brands":brands,
        "meta": meta,
    }
    return render(request, "web/brand.html", context)

# def product_category(request):
#     product_categories = ProductCategory.objects.all()
#     context = {
#         "product_categories":product_categories
#     }
#     return render(request, "web/category.html", context)


def product(request):
    meta = Meta.objects.filter(page="products").first()
    brand_slug = request.GET.get('brand')
    category_slug = request.GET.get('category')

    product_categories = ProductCategory.objects.annotate(product_count=Count('product'))

    products = Product.objects.all()

    if brand_slug:
        products = products.filter(brand__slug=brand_slug)

    if category_slug:
        products = products.filter(category__slug=category_slug)

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "is_products": True,
        "products": page_obj,
        "page_obj": page_obj,
        "selected_brand": brand_slug,
        "selected_category": category_slug,
        "product_categories": product_categories,
        "total_products_count": Product.objects.count(),
        "meta":meta,
    }
    return render(request, "web/product.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    other_products = Product.objects.exclude(slug=slug, category=product.category)[:6]

    if request.method == "POST":
        form = ProductEnquiryForm(request.POST)

        turnstile_token = request.POST.get('cf-turnstile-response')
        captcha_data = {
            'secret': settings.CLOUDLFAIR_TURNSTILE_PRIVATE_KEY,
            'response': turnstile_token,
        }

        captcha_response = requests.post(
            'https://challenges.cloudflare.com/turnstile/v0/siteverify',
            data=captcha_data
        )
        captcha_result = captcha_response.json()

        if captcha_result.get('success'):
            if form.is_valid():
                enquiry = form.save(commit=False)
                enquiry.product = product
                enquiry.save()

                # Send email
                subject = f"Product Enquiry for {product.title}"
                message = (
                    f'Name: {enquiry.name}\n'
                    f'Email: {enquiry.email}\n'
                    f'Phone: {enquiry.phone}\n'
                    f'Quantity: {enquiry.quantity}\n'
                    f'Message: {enquiry.message}\n'
                )
                from_email = enquiry.email
                recipient_list = ["info@speedandsafetrading.com"]

                email = EmailMessage(subject, message, from_email, recipient_list)
                email.send(fail_silently=False)

                # WhatsApp URL
                whatsapp_text = (
                    f"Product Enquiry for *{product.title}*%0A"
                    f"Name: {enquiry.name}%0A"
                    f"Email: {enquiry.email}%0A"
                    f"Phone: {enquiry.phone}%0A"
                    f"Quantity: {enquiry.quantity}%0A"
                    f"Message: {enquiry.message}"
                )
                whatsapp_url = f"https://wa.me/+971509846948?text={whatsapp_text}"

                return JsonResponse({
                    "status": "true",
                    "title": "Successfully Submitted",
                    "message": "Message successfully sent",
                    "whatsapp_url": whatsapp_url,
                })
            else:
                return JsonResponse({
                    "status": "false",
                    "title": "Form validation error",
                    "message": "Please ensure all fields are filled out correctly.",
                    "errors": form.errors  
                })

        return JsonResponse({
            "status": "false",
            "title": "CAPTCHA verification failed",
            "message": "Please complete the CAPTCHA correctly."
        })

    else:
        form = ProductEnquiryForm()

    context = {
        "product": product,
        "other_products": other_products,
        "form": form,
        "turnstile_site_key": settings.CLOUDLFAIR_TURNSTILE_PUBLIC_KEY,
    }
    return render(request, "web/product-details.html", context)


def blog(request):
    meta = Meta.objects.filter(page="blogs").first()
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "is_blogs":True,
        "page_obj": page_obj,
        "meta":meta,
    }
    return render(request, "web/blog.html", context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    other_blogs = Blog.objects.exclude(slug=slug)

    context = {
        "blog": blog,
        "other_blogs":other_blogs,
    }
    return render(request, "web/blog-details.html", context)


def contact(request):
    meta = Meta.objects.filter(page="contact").first()
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        turnstile_response = request.POST.get('cf-turnstile-response')
        data = {
            'secret': settings.CLOUDLFAIR_TURNSTILE_PRIVATE_KEY, 
            'response': turnstile_response,
        }
        
        captcha_response = requests.post('https://challenges.cloudflare.com/turnstile/v0/siteverify', data=data)
        captcha_result = captcha_response.json()

        if captcha_result.get('success'):
            if form.is_valid(): 
                data = form.save()

                subject = f"Contact Enquiry"
                message = (
                    f'Name: {data.name} \n'
                    f'Email: {data.email}\n'
                    f'Phone: {data.phone}\n' 
                    f'Subject: {data.subject}\n'
                    f'Message: {data.message}\n'
                )
                from_email = data.email
                recipient_list = ["info@speedandsafetrading.com"]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                # WhatsApp Message
                whatsapp_message = (
                    f"Name: {data.name}%0A"
                    f"Email: {data.email}%0A"
                    f"Phone: {data.phone}%0A"
                    f"Subject: {data.subject}%0A"
                    f"Message: {data.message}"
                )
                whatsapp_url = f"https://wa.me/+971509846948?text={whatsapp_message}" 

                response_data = {
                    "status": "true",
                    "title": "Successfully Submitted",
                    "message": "Message successfully sent",
                    "whatsapp_url": whatsapp_url,  
                }
                return JsonResponse(response_data)
            else:
                response_data = {
                    "status": "false",
                    "title": "Form validation error",
                    "message": "Please ensure all fields are filled out correctly."
                }
                return JsonResponse(response_data)

        else:
            response_data = {
                "status": "false",
                "title": "CAPTCHA verification failed",
                "message": "Please complete the CAPTCHA correctly."
            }
            return JsonResponse(response_data)

    else:
        form = ContactForm()
        context = {
            "is_contact": True,
            "form": form,
            "turnstile_site_key": settings.CLOUDLFAIR_TURNSTILE_PUBLIC_KEY,
            "meta":meta,
        }
        return render(request, "web/contact.html", context)