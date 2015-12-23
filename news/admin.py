from django.contrib import admin
from django import forms
from models import News
from tinymce.widgets import TinyMCE

# Register your models here.


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols':75, 'rows':30}))


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'author', 'timestamp')
    fields = ('title', 'brief', 'content', 'headimg', 'published')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user.userprofile
        obj.save()
