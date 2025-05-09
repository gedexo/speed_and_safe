from .models import Product

def main_context(request):
    footer_products = Product.objects.all()
    return {
        "footer_products": footer_products
    }