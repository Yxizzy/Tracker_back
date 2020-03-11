from django.contrib import admin
from .models import Product, Tracker, Status
# Register your models here.
admin.site.register(Product)
admin.site.register(Tracker)
admin.site.register(Status)
