from datetime import datetime
from django.db import models
from django.utils.html import format_html
from mdeditor.fields import MDTextField


class Tag(models.Model):
    """
    Tag
    """
    name = models.CharField(max_length=30, verbose_name='name')

    # 统计文章数 并放入后台
    def get_items(self):
        return len(self.article_set.all())

    get_items.short_description = 'tag'

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Category
    """
    name = models.CharField(max_length=30, verbose_name='name')
    index = models.IntegerField(default=99, verbose_name='index')
    active = models.BooleanField(default=True, verbose_name='active')
    icon = models.CharField(max_length=30, default='fa-home',verbose_name='icon')

    # 统计文章数 并放入后台
    def get_items(self):
        return len(self.article_set.all())

    def icon_data(self):
        return format_html(
            '<i class="{}"></i>',
            self.icon,
        )

    get_items.short_description = 'category items'
    icon_data.short_description = 'icons for category'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Article
    """
    title = models.CharField(max_length=50, verbose_name='title')
    desc = models.TextField(max_length=100, verbose_name='description')
    cover = models.CharField(max_length=200, default='https://image.3001.net/images/20200304/15832956271308.jpg', verbose_name='cover')
    content = MDTextField(verbose_name='content')
    click_count = models.IntegerField(default=0, verbose_name='click_count')
    is_recommend = models.BooleanField(default=False, verbose_name='is_recommend')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add_time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update_time')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='category', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='tag')

    def cover_data(self):
        return format_html(
            '<img src="{}" width="156px" height="98px"/>',
            self.cover,
        )

    def cover_admin(self):
        return format_html(
            '<img src="{}" width="440px" height="275px"/>',
            self.cover,
        )

    def viewed(self):
        """
        times viewed
        """
        self.click_count += 1
        self.save(update_fields=['click_count'])

    cover_data.short_description = 'cover image'
    cover_admin.short_description = 'cover image'

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Comment
    """
    content = models.TextField(verbose_name='content')
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='username')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='add_time')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='article', on_delete=models.CASCADE)
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='pid', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:20]


class Links(models.Model):
    """
    Links
    """
    title = models.CharField(max_length=50, verbose_name='title')
    url = models.URLField(verbose_name='url')
    desc = models.TextField(verbose_name='desc', max_length=250)
    image = models.URLField(default='https://image.3001.net/images/20190330/1553875722169.jpg', verbose_name='image')

    def avatar_data(self):
        return format_html(
            '<img src="{}" width="50px" height="50px" style="border-radius: 50%;" />',
            self.image,
        )

    def avatar_admin(self):
        return format_html(
            '<img src="{}" width="250px" height="250px"/>',
            self.image,
        )

    avatar_data.short_description = 'blog avatar'
    avatar_admin.short_description = 'admin avatar'

    class Meta:
        verbose_name = 'links'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.url


class Site(models.Model):
    """
    Site
    """
    desc = models.CharField(max_length=50, verbose_name='desc')
    keywords = models.CharField(max_length=50, verbose_name=' keywords')
    title = models.CharField(max_length=50, verbose_name='title')
    index_title = models.CharField(max_length=50, verbose_name='index_title')
    type_chinese = models.CharField(max_length=50, verbose_name='type_chinese')
    type_english = models.CharField(max_length=80, verbose_name='type_english')
    icp_number = models.CharField(max_length=20, verbose_name='icp_number')
    icp_url = models.CharField(max_length=50, verbose_name='icp_url')
    site_mail = models.CharField(max_length=50, verbose_name='site_mail')
    site_qq = models.CharField(max_length=50, verbose_name='site_qq')
    site_avatar = models.CharField(max_length=200, default='https://image.3001.net/images/20171226/15142933784705.png', verbose_name='site_avatar')

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
