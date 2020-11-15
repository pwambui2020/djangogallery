from django.contrib import admin
from .models import Images, Location,Category
# Register your models here.
# class ImageAdmin(admin.ModelAdmin):
#     filter_horizontal =('images',)

admin.site.register(Images)
admin.site.register(Location)
admin.site.register(Category)