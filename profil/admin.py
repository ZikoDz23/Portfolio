from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(ProjectImages)
admin.site.register(Skills)