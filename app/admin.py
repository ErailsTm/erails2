from django.contrib import admin
from . models import Category,Products,ProductImage
# Register your models here.
admin.site.register([Category,Products,ProductImage])