from django.shortcuts import render

from .models import Tag

# Create your views here.

def index(request):
    """the home page for Etergram"""
    return render(request, 'etergrams/index.html')


def tags(request):
    """show all tags"""
    tags = Tag.objects.order_by('date_added')
    context = {'tags': tags}
    return render(request, 'etergrams/tags.html', context)


def tag(request, tag_id):
    """show all entries for a single tag"""
    tag = Tag.objects.get(id=tag_id)
    entries = tag.entry_set.all()#('-date_added')
    context = {'tag': tag, 'entries': entries}
    return render(request, 'etergrams/tag.html', context)
