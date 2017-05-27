from django.contrib import admin

# Register your models here.
from etergrams.models import Tag
from etergrams.models import Entry

admin.site.register(Tag)
admin.site.register(Entry)
