from .models import ProductCategory

def main_context(request):
    footer_categories = ProductCategory.objects.all()[:8]
    return {
        "footer_categories": footer_categories
    }