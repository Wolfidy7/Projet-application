from django.contrib import admin
from authentication.models import *
from blog.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Subject)