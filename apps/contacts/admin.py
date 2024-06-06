from django.contrib import admin
from apps.contacts.models import *


# Register your models here.


class ContactFilterAdmin(admin.ModelAdmin):
    list_filter = ('name','email')
    list_display = ('name','email', 'phone', )
    search_fields = ('name',)
    readonly_fields = ('name','email','phone','message')

admin.site.register(Contacts, ContactFilterAdmin)
admin.site.register(Journal)
admin.site.register(Expert)