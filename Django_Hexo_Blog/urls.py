from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views import static

from blog.views import Index, Friends, Detail, Archive, CategoryList, CategoryView, TagList, TagView, About

urlpatterns = [
    path('admin/', admin.site.urls),

    # 首页
    path('', Index.as_view(), name='index'),

    # 友情链接
    path('friends/', Friends.as_view(), name='friends'),

    # 后台 markdown 编辑器配置
    path('mdeditor/', include('mdeditor.urls')),

    # 文章归档
    path("article/", Archive.as_view(), name='archive'),

    # 文章详情
    path('article/<int:pk>', Detail.as_view(), name='detail'),

    # 分类统计
    path('category/', CategoryList.as_view(), name='category'),

    # 文章分类
    path('category/<int:pk>', CategoryView.as_view(), name='article_category'),

    # 标签统计
    path('tag/', TagList.as_view(), name='tag'),

    # 文章标签
    path('tag/<int:pk>', TagView.as_view(), name='article_tag'),

    # 关于本站
    path('about/', About.as_view(), name='about'),

    # 静态文件
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }, name='static')
]

# 设置后台名称
admin.site.site_header = '国光博客后台'
admin.site.site_title = 'Django Blog 后台'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)