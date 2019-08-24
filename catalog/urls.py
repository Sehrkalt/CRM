from django.urls import path
from catalog.views.user_views import cabinet
from catalog.views.user_views import contractor
from catalog.views.user_views import deal_type
from catalog.views.user_views import position
from catalog.views.user_views import project
from catalog.views.user_views import remains_of_goods
from catalog.views.user_views import scope
from catalog.views.user_views import task
from catalog.views.user_views import user_views


urlpatterns = [
    path('', user_views.index, name='index'),
]

urlpatterns += [
    path('cabinet', cabinet.user_cabinet, name='user_cabinet'),
    path('cabinet/companies', user_views.companies, name='company_list'),
    path('cabinet/contractors', contractor.contractors, name='contractor_list'),
    path('cabinet/countries', user_views.countries, name='country_list'),
    path('cabinet/dealtypes', deal_type.deal_types, name='deal_type_list'),
    path('cabinet/departments', user_views.departments, name='department_list'),
    path('cabinet/manufacturers', user_views.manufacturers, name='manufacturer_list'),
    path('cabinet/product_categories', user_views.product_categories, name='product_category_list'),
    path('cabinet/units', user_views.units, name='unit_list'),
    path('cabinet/products', user_views.products, name='product_list'),
    path('cabinet/positions', position.positions, name='position_list'),
    path('cabinet/projects', project.projects, name='project_list'),
    path('cabinet/remains', remains_of_goods.remains_of_goods, name='remains_of_goods'),
    path('cabinet/scopes', scope.scopes, name='scope_list'),
    path('cabinet/tasks', task.tasks, name='task_list'),

    path('cabinet/employees', user_views.employees, name='employee_list'),

]