from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

about_inf = {'Имя': 'Юрий',
             'Отчество': 'Александрович',
             'Фамилия': 'Сыновец',
             'телефон': '8-919-000-00-00',
             'email': 'exampel@mail.ru'}

items_inf = [
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]


def home(render):
    text = '''<h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Сыновец Ю.А.</i>
    <a href="http://127.0.0.1:8000/items/">items</a>
    <a href="http://127.0.0.1:8000/about/">about</a>
    '''
    return HttpResponse(text)


def about(render):
    text = f'''<p>Имя: <b>{about_inf.get('Имя')}</b></p>
    <p>Отчество: <b>{about_inf.get('Отчество')}</b></p>
    <p>Фамилия: <b>{about_inf.get('Фамилия')}</b></p>
    <p>телефон: <b>{about_inf.get('телефон')}</b></p>
    <p>email: <b>{about_inf.get('email')}</b></p>
    '''
    return HttpResponse(text)


def item(render, id=1):
    for dictt in items_inf:
        if dictt.get('id') == id:
            html = f'''<a href="http://127.0.0.1:8000/items/">назад к списку товаров</a>.
            <table style="border-collapse: collapse; width: 100%;" border="1">
                <tbody>
                    <tr>
                        <td style="width: 50%;">{dictt.get('id')}</td>
                        <td style="width: 50%;">{dictt.get('name')}</td>
                    </tr>
                </tbody>
            </table>
            '''
            return HttpResponse(html)
    return HttpResponse(f'Тавар с id={id} не существует')


def items(render):
    table = '''
    <table style="border-collapse: collapse; width: 100%;" border="1">
      <tbody>
    '''
    for item in items_inf:
        table += f'''<tr>
            <td style="width: 50%;"><a href="http://127.0.0.1:8000/item/{item.get('id')}">{item.get('id')}</a></td>
            <td style="width: 50%;">{item.get('name')}</td>
        </tr>
        '''
    table += '''
          </tbody>
        </table>
        '''

    return HttpResponse(table)
