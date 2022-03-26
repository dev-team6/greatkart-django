from .models import Category

def menu_link(request):
    links = Category.objects.all()
    context = {
        'links':links
    }
    return context
