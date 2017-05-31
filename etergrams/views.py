from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Tag
from .forms import TagForm
from .models import Entry
from .forms import EntryForm

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


# def new_entry(request, tag_id):
#     """add a new entry to a particular tag"""
#     tag = Tag.objects.get(id=tag_id)
#
#     if request.method != 'POST':
#         form = EntryForm()
#     else:
#         form = EntryForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_entry = form.save(commit=False)
#             new_entry.tag = tag
#             #m = ExampleModel.objects.get(pk=course_id)
#             #new_entry.model_pic = form.cleaned_data['image']
#             new_entry.save()
#             return HttpResponseRedirect(reverse('etergrams:tag', args=[tag_id]))
#
#     context = {'tag': tag, 'form': form}
#     return render(request, 'etergrams/new_entry.html', context)

def new_entry(request):
    """add a new entry to some tags"""
    #tags = Entry.tag.all()
    tags = []
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(request.POST, request.FILES, request.POST)
        if form.is_valid():
            tags = Entry.tag.all()
            #tags = .tag.all()
            new_entry = form.save(commit=False)
            #new_entry.tag = tags
            new_entry.save()
            return HttpResponseRedirect(reverse('etergrams:tags'))

    #context = {'tag': tag, 'form': form}
    context = {'form': form, 'tag': tag}
    return render(request, 'etergrams/new_entry.html', context)
