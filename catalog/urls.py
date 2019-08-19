from django.urls import path
from catalog.views import user_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', user_views.index, name='index'),
]

urlpatterns += [
    path('cabinet', user_views.user_cabinet, name='user_cabinet'),
    path('cabinet/companies', user_views.companies, name='company_list'),
    path('cabinet/departments', user_views.departments, name='department_list'),
    path('cabinet/countries', user_views.countries, name='country_list'),

    path('cabinet/employees', user_views.employees, name='employee_list'),

]