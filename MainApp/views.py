from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm, UserRegistrationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.models import User

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


@login_required
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
                messages.success(request, 'Snippet created')
            return redirect('snippets-my-list')
        messages.warning(request, 'Snippet not created')
        return render(request,'pages/form_snippet.html',{'form': form})


def snippets_page(request):
    data = Snippet.objects.filter(public=True)
    users = User.objects.all()
    if request.user.is_authenticated:
        data = data | Snippet.objects.filter(user=request.user, public=False)
    context = {'pagename': 'Просмотр сниппетов',
               'snippets': data,
               'users': users}
    return render(request, 'pages/view_snippets.html', context)


def snippets_detail(request, id=0):
    try:
        snippet = Snippet.objects.get(id=id)
        context = {'pagename': 'Просмотр кода сниппета',
                   'snippet': snippet}
        return render(request, 'pages/view_snippets_detail.html', context)
    except Exception as err:
        print(f'to log? get item id={id} err: {err}')
        return HttpResponse(f'Snippet с id={id} не существует')


@login_required
def snippets_change(request, id):
    if request.method == 'GET':
        snipper = Snippet.objects.get(id=id)
        form = SnippetForm(instance=snipper)
        context = {'pagename': 'Изменение сниппета',
                   'form': form,
                   'butoon': 'Изменить',
                   'tid': id}
        return render(request, 'pages/form_snippet.html', context)

    if request.method == 'POST':
        try:
            form = Snippet.objects.get(id=id)
            form.name = request.POST.get('name')
            form.lang = request.POST.get('lang')
            form.code = request.POST.get('code')
            if request.POST.get('public') == 'on':
                form.public = True
            else:
                form.public = False
            form.save()
            messages.success(request, 'Snippet changed')
            return redirect('snippets-my-list')
        except ObjectDoesNotExist:
            messages.error(request, 'Snippet not changed')
            raise Http404


@login_required
def snippet_delete(request, id):
    spippet = Snippet.objects.get(id=id)
    spippet.delete()
    messages.success(request, 'Snippet deleted')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def create_user(request):
    context = {'pagename': 'Регистрация'}
    if request.method == 'GET':
        form = UserRegistrationForm()
        context['form'] = form
        return render(request, 'pages/registration.html', context)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created')
            return redirect('home')
        context['form'] = form
        messages.warning(request, 'User not created')
        return render(request, 'pages/registration.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'User login')
        else:
            context = {'pagename': 'PythonBin',
                       'errors': ['wrong user or password']}
            messages.warning(request, 'wrong user or password')
            return render(request, 'pages/index.html', context)
    return redirect('home')


def loguot(request):
    auth.logout(request)
    messages.info(request, 'User loguot')
    return redirect('home')


@login_required
def snippets_my_list(request):
    snippets = Snippet.objects.filter(user=request.user)
    context = {'pagename': 'Мои сниппеты',
               'snippets': snippets,
               'user': request.user}
    return render(request, 'pages/view_snippets.html', context)

def listsort(request):
    colum = request.GET.get('sort')
    abc = int(request.GET.get('abc'))
    user = request.GET.get('user')
    if user:
        snippets = Snippet.objects.filter(user=user)
    else:
        snippets = Snippet.objects.all().order_by(colum)
    if abc:
        snippets = snippets.order_by(colum)
    else:
        snippets = snippets.order_by(f'-{colum}')
    users = User.objects.all()
    context = {'pagename': 'Мои сниппеты',
               'snippets': snippets,
               'user': user,
               'users': users}
    return render(request, 'pages/view_snippets.html', context)

def listsortuser(request):
    if request.method == 'POST':
        sort_user = request.POST.get('sort_user')
        snippets = Snippet.objects.filter(user__username=sort_user)
        users = User.objects.all()
        context = {'pagename': 'Мои сниппеты',
                   'snippets': snippets,
                   'users': users}
        return render(request, 'pages/view_snippets.html', context)
    else:
        return Http404
