from django.urls import path
from catalog.views.user_views import cabinet
from catalog.views.user_views.lists import scope_list, project_list, deal_type_list, remains_of_goods_list, \
    contractor_list, deal_list, position_list, task_list, company_list, country_list, department_list, manufacturer_list, \
    unit_list, employee_list

from catalog.views.user_views.category import product_category_list, category_add

from catalog.views.user_views.product import product_list, product_add

from catalog.views import registration
from catalog.views.landing import index
urlpatterns = [
    path('', index.index, name='index'),
]

urlpatterns += [
    path('cabinet', cabinet.user_cabinet, name='user_cabinet'),
    path('cabinet/companies', company_list.companies, name='company_list'),
    path('cabinet/contractors', contractor_list.contractors, name='contractor_list'),
    path('cabinet/countries', country_list.countries, name='country_list'),
    path('cabinet/deals', deal_list.deals, name='deal_list'),
    path('cabinet/dealtypes', deal_type_list.deal_types, name='deal_type_list'),
    path('cabinet/departments', department_list.departments, name='department_list'),
    path('cabinet/manufacturers', manufacturer_list.manufacturers, name='manufacturer_list'),
    path('cabinet/units', unit_list.units, name='unit_list'),
    path('cabinet/positions', position_list.positions, name='position_list'),
    path('cabinet/projects', project_list.projects, name='project_list'),
    path('cabinet/remains', remains_of_goods_list.remains_of_goods, name='remains_of_goods'),
    path('cabinet/scopes', scope_list.scopes, name='scope_list'),
    path('cabinet/tasks', task_list.tasks, name='task_list'),
    path('cabinet/employees', employee_list.employees, name='employee_list'),



    path('cabinet/product_categories/add', category_add.CategoryCreate.as_view(), name='category_add'),
    path('cabinet/product_categories', product_category_list.product_categories, name='product_category_list'),

    path('cabinet/products/add', product_add.ProductCreate.as_view(), name='product_add'),
    path('cabinet/products', product_list.products, name='product_list'),

    path('registration', registration.RegisterFormView.as_view(), name='registration'),

]