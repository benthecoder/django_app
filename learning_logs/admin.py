from django.contrib import admin

from .models import Topic, Entry
# Register your models here.

from .models import Topic # look for models

admin.site.register(Topic) # tells django to manage model through admin site
admin.site.register(Entry)
