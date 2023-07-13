from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
from MainApp.models import Snippet
from MainApp.forms import SnippetForm

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета',
                   'form': form}
        return render(request, 'pages/add_snippet.html', context)

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippets-list')
        return render(request,'pages/add_snippet.html',{'form': form})


def snippets_page(request):
    context = {'pagename': 'Просмотр сниппетов',
               'snippets': Snippet.objects.all()}
    return render(request, 'pages/view_snippets.html', context)


def snippets_detail(request, id=0):
    try:
        context = {'pagename': 'Просмотр кода сниппета',
                   'snippet': Snippet.objects.get(id=id)}
        return render(request, 'pages/view_snippets_detail.html', context)
    except Exception as err:
        print(f'to log? get item id={id} err: {err}')
        return HttpResponse(f'Snippet с id={id} не существует')

#def snippets_create(request):
#    if request.method == 'POST':
#        name = request.POST['name']
#        lang = request.POST['lang']
#        code = request.POST['code']
#        data = Snippet(name=name, lang=lang, code=code)
#        data.save()
#        return redirect('snippets-list')
