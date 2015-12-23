from django.contrib import admin
from models import News

# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'timestamp')
    fields = ('title', 'brief', 'content', 'headimg', 'published')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user.userprofile
        obj.save()
