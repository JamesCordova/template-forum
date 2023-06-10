from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(SubPost)
admin.site.register(Response)
admin.site.register(Topic)

