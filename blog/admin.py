from django.contrib import admin
from .models import AboutUs, Post,Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(AboutUs)