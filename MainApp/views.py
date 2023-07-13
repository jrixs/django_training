from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета',
                   'form': form,
                   'butoon': 'Создать'}
        return render(request, 'pages/form_snippet.html', context)

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
            return redirect('snippets-list')
        return render(request,'pages/form_snippet.html',{'form': form})


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


def snippets_change(request, id):
    if request.method == 'GET':
        snipper = Snippet.objects.get(id=id)
        form = SnippetForm(instance=snipper)
        context = {'pagename': 'Изменение сниппета',
                   'form': form,
                   'butoon': 'Изменить'}
        return render(request, 'pages/form_snippet.html', context)

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippets-list')
        return render(request,'pages/form_snippet.html', {'form': form})


def snippet_delete(request, id):
    spippet = Snippet.objects.get(id=id)
    spippet.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass
    return redirect('home')


def loguot(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))

