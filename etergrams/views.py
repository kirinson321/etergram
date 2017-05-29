from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Tag
from .forms import TagForm

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


def new_tag(request):
    """add a new tag"""
    if request.method != 'POST':
        form = TagForm()
    else:
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('etergrams:tags'))

    context = {'form': form}
    return render(request, 'etergrams/new_tag.html', context)
