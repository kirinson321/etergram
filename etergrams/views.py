from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, Http404
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
    entries = tag.entry_set.order_by('-date_added')
    context = {'tag': tag, 'entries': entries}
    return render(request, 'etergrams/tag.html', context)

@login_required
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

#damn, this one below took me a full day to work out; had to bite into POST requests for it to fully working
@login_required
def new_entry(request):
    """add a new entry to some tags"""
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            tags = request.POST.getlist('tag', '')
            for each in tags:
                new_entry.tag.add(each)
                new_entry.save()
            new_entry.save()
            return HttpResponseRedirect(reverse('etergrams:tags'))

    context = {'tag': tag, 'form': form}
    return render(request, 'etergrams/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)

    if entry.owner != request.user:
        raise Http404


    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('etergrams:tags'))

    context = {'entry': entry, 'form': form}
    return render(request, 'etergrams/edit_entry.html', context)
