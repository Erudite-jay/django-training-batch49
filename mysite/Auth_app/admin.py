from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Contact)

# @admin.register(models.Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ("id",'fullname', 'email', 'phone', 'message')
#     search_fields = ('fullname', 'email', 'phone', 'message')
#     list_filter = ('fullname', 'email', 'phone', 'message')