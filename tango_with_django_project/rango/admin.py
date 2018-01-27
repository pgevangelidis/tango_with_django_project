from django.contrib import admin
from rango.models import Category, Page
# Register your models here.

#admin.site.register(Category)

#Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

#Update the registration to include this customised Interface
admin.site.register(Category, CategoryAdmin)


admin.site.register(Page)
