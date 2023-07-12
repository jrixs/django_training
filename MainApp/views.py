from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, request
from MainApp.models import Item


# Create your views here.

about_inf = {'name': 'Юрий',
             'patronymic': 'Александрович',
             'surname': 'Сыновец',
             'tel': '8-919-000-00-00',
             'email': 'exampel@mail.ru'}


def home(request):
    context = {
        'name': 'Сыновец Юрий Александрович',
        'email': 'exampel@mail.ru'
    }
    return render(request=request, template_name='index.html', context=context)


def about(request):
    return render(request=request, template_name='about.html', context=about_inf)


def item(request, id=1):
    try:
        return render(request=request, template_name='item_page.html', context={'item': Item.objects.get(id=id)})
    except Exception as err:
        print(f'to log? get item id={id} err: {err}')
        return HttpResponse(f'Тавар с id={id} не существует')


def items(request):
    return render(request=request, template_name='items_list.html', context={'items': Item.objects.all()})
