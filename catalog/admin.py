from django.contrib import admin
# Register your models here.

from catalog.models.profile import Profile
from catalog.models.company import Company
from catalog.models.department import Department
from catalog.models.country import Country
from catalog.models.manufacturer import Manufacturer
from catalog.models.product import Product
from catalog.models.unit import Unit
from catalog.models.product_category import ProductCategory


# Define the admin class
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'position', 'phone')

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ('name', 'scope', )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ('name', 'scope', )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ('name', )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer
    list_display = ('name', 'country')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'category', 'manufacturer', 'units',)


@admin.register(Unit)
class UnitsAdmin(admin.ModelAdmin):
    model = Unit
    list_display = ('name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    list_display = ('name',)
