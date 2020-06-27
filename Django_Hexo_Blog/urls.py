from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views import static

from blog.views import Index, Friends, Detail, Archive, CategoryList, CategoryView, TagList, TagView, About

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('friends/', Friends.as_view(), name='friends'),
    path('mdeditor/', include('mdeditor.urls')),
    path("article/", Archive.as_view(), name='archive'),
    path('article/<int:pk>', Detail.as_view(), name='detail'),
    path('category/', CategoryList.as_view(), name='category'),
    path('category/<int:pk>', CategoryView.as_view(), name='article_category'),
    path('tag/', TagList.as_view(), name='tag'),
    path('tag/<int:pk>', TagView.as_view(), name='article_tag'),
    path('about/', About.as_view(), name='about'),
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }, name='static')
]

admin.site.site_header = 'Mi Primer Blog'
admin.site.site_title = 'Django Blog app'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)