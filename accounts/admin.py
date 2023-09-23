from django.contrib import admin

# Register your models here.
from .models import Profile, Phones, Address


class PhonesAdmin(admin.TabularInline):
    model = Phones



class AddressAdmin(admin.TabularInline):
    model = Address



class ProfilAdmin(admin.ModelAdmin):
    #inlines = [PhonesAdmin,AddressAdmin]
    pass




admin.site.register(Profile, ProfilAdmin)
admin.site.register(Phones)
admin.site.register(Address)