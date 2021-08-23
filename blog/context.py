from .models import Category

def related(request):
    context = {
        'category_list': Category.objects.all(),
        #'tag_list': Tag.objects.all(),
    }
    return context