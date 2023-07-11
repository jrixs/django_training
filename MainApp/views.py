from django.shortcuts import render
from django.http import HttpResponseNotFound
from MainApp.data import countries, chars
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    return render(request=request, template_name='index.html')


def countries_list(request):
    paginator = Paginator([x.get('country') for x in countries], 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request,
                  template_name='countries_list.html',
                  context={'countries': page_obj, 'chars': chars})


def country(request, name_country=''):
    for country in countries:
        if country.get('country') == name_country:
            return render(request=request, template_name='country.html', context={'country': country})
    return HttpResponseNotFound(f'Country {name_country} not found!')



def country_filter(request, char=''):
    result: list = []
    for country in countries:
        if country.get('country')[:1].upper() == char.upper():
            result.append(country.get('country'))
    if result:
        return render(request=request, template_name='countries_list.html',
                      context={'countries': result,
                           'chars': chars})
    return HttpResponseNotFound(f'Country {char} not found!')


def languages_list(request):
    result: list = []
    for country in countries:
        if len(country.get('languages')) > 0:
            for language in country.get('languages'):
                if language not in result:
                    result.append(language)

    return render(request=request,
                  template_name='languages_list.html',
                  context={'countries': sorted(result),
                           'chars': chars})


def language(request, name_language=''):
    result: list = []
    for country in countries:
        if name_language in country.get('languages'):
            result.append(country.get('country'))
    if result:
        return render(request=request, template_name='language.html',
                      context={'countrys': result, 'language': name_language})
    return HttpResponseNotFound(f'Language {name_language} not found!')
