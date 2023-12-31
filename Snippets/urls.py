from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='snippets-add'),
    path('snippets/list', views.snippets_page, name='snippets-list'),
    path('snippets/<int:id>', views.snippets_detail, name='snippet-detail'),
    path('snippets/<int:id>/change', views.snippets_change, name='snippet-change'),
    path('snippet/<int:id>/delete', views.snippet_delete, name='snippet-delete'),
    path('snippets/my', views.snippets_my_list, name='snippets-my-list'),
    path('login', views.login, name='login'),
    path('logout', views.loguot, name='loguot'),
    path('auth/register', views.create_user, name='register'),
    path('listsort', views.listsort, name='listsort'),
    path('snippet/user/sort', views.listsortuser, name='snippet-user-sort')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
