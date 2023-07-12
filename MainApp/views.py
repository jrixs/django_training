from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, request
from MainApp.models import Item


# Create your views here.

about_inf = {'Имя': 'Юрий',
             'Отчество': 'Александрович',
             'Фамилия': 'Сыновец',
             'телефон': '8-919-000-00-00',
             'email': 'exampel@mail.ru'}


def home(request):
    context = {
        'name': 'Сыновец Юрий Александрович',
        'email': 'exampel@mail.ru'
    }
    return render(request=request, template_name='index.html', context=context)


def about(request):
    text = f'''<p>Имя: <b>{about_inf.get('Имя')}</b></p>
    <p>Отчество: <b>{about_inf.get('Отчество')}</b></p>
    <p>Фамилия: <b>{about_inf.get('Фамилия')}</b></p>
    <p>телефон: <b>{about_inf.get('телефон')}</b></p>
    <p>email: <b>{about_inf.get('email')}</b></p>
    '''
    return HttpResponse(text)


def item(request, id=1):
    try:
        return render(request=request, template_name='item_page.html', context={'item': Item.objects.get(id=id)})
    except Exception as err:
        print(f'to log? get item id={id} err: {err}')
        return HttpResponse(f'Тавар с id={id} не существует')


def items(request):
    return render(request=request, template_name='items_list.html', context={'items': Item.objects.all()})
