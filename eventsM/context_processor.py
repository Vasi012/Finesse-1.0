from .models import Category


def extras(request):
    """Create a rule to show edit and preview profile for users"""
    categories = Category.objects.all()

    return {'categories': categories}
