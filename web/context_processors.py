from .models import Product

def main_context(request):
    footer_products = Product.objects.all()[:8]
    return {
        "footer_products": footer_products
    }