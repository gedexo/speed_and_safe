from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


from .models import Banner, Blog


def index(request):
    banners = Banner.objects.all()
    context = {"is_index": True, "banners":banners}
    return render(request, "web/index.html", context)


def about(request):
    return render(request, "web/about.html")


def service(request):
    return render(request, "web/service.html")


def blog(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }
    return render(request, "web/blog.html", context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    other_blogs = Blog.objects.exclude(slug=slug)

    context = {
        "blog": blog,
        "other_blogs":other_blogs,
    }
    return render(request, "web/blog-detail.html", context)


def contact(request):
    return render(request, "web/contact.html")