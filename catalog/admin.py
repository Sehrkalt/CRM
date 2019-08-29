from django.contrib import admin
# Register your models here.

from catalog.models.company import Company
from catalog.models.companies_in_profile import CompaniesInProfile
from catalog.models.country import Country
from catalog.models.contractor import Contractor
from catalog.models.deal_type import DealType
from catalog.models.department import Department
from catalog.models.manufacturer import Manufacturer
from catalog.models.position import Position
from catalog.models.product import Product
from catalog.models.category import ProductCategory
from catalog.models.profile import Profile
from catalog.models.project import Project
from catalog.models.remains_of_goods import RemainsOfGoods
from catalog.models.scope import Scope
from catalog.models.scopes_in_company import ScopesInCompany
from catalog.models.task import Task
from catalog.models.unit import Unit


# Define the admin class
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'position', 'phone')

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ('name', )


@admin.register(CompaniesInProfile)
class CompaniesInProfileAdmin(admin.ModelAdmin):
    model = CompaniesInProfile
    list_display = ('profile', 'company', )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ('name', )


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    model = Contractor
    list_display = ('name', )


@admin.register(DealType)
class DealTypeAdmin(admin.ModelAdmin):
    model = DealType
    list_display = ('name', )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ('name', 'scope', )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer
    list_display = ('name', 'country')


@admin.register(Position)
class PositionsAdmin(admin.ModelAdmin):
    model = Position
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'category', 'manufacturer', 'units',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    list_display = ('name',)


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'responsible', 'status', 'date')


@admin.register(RemainsOfGoods)
class RemainsOfGoodsAdmin(admin.ModelAdmin):
    model = RemainsOfGoods
    list_display = ('product', 'count')


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    model = Scope
    list_display = ('name',)


@admin.register(ScopesInCompany)
class ScopesInCompanyAdmin(admin.ModelAdmin):
    model = ScopesInCompany
    list_display = ('company', 'scope')


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('name', 'responsible', 'project', 'status', 'date')


@admin.register(Unit)
class UnitsAdmin(admin.ModelAdmin):
    model = Unit
    list_display = ('name',)

