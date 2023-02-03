from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Area, Cords, MountainPass, Photo


class CustomMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20


admin.site.register(Photo)
admin.site.register(MountainPass)
admin.site.register(Area, MPTTModelAdmin)
admin.site.register(Cords)
