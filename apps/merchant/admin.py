from django.contrib import admin
from .models import Merchant, Store, Catalog

# Register your models here.
admin.site.register(Merchant)
admin.site.register(Store)
admin.site.register(Catalog)