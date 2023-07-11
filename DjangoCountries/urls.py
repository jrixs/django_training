from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('countries-list', views.countries_list),
    path('languages-list', views.languages_list),
    path('country/<str:name_country>', views.country),
    path('language/<str:name_language>', views.language),
    path('country-filter/<str:char>', views.country_filter),
]
