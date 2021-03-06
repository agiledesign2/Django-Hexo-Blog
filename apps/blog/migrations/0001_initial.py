# Generated by Django 2.2.12 on 2020-05-28 22:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('desc', models.TextField(max_length=100, verbose_name='description')),
                ('cover', models.CharField(default='https://image.3001.net/images/20200304/15832956271308.jpg', max_length=200, verbose_name='cover')),
                ('content', mdeditor.fields.MDTextField(verbose_name='content')),
                ('click_count', models.IntegerField(default=0, verbose_name='click_count')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='is_recommend')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'article',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('index', models.IntegerField(default=99, verbose_name='index')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('icon', models.CharField(default='fa-home', max_length=30, verbose_name='icon')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'category',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('url', models.URLField(verbose_name='url')),
                ('desc', models.TextField(max_length=250, verbose_name='desc')),
                ('image', models.URLField(default='https://image.3001.net/images/20190330/1553875722169.jpg', verbose_name='image')),
            ],
            options={
                'verbose_name': 'links',
                'verbose_name_plural': 'links',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=50, verbose_name='desc')),
                ('keywords', models.CharField(max_length=50, verbose_name=' keywords')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('index_title', models.CharField(max_length=50, verbose_name='index_title')),
                ('type_chinese', models.CharField(max_length=50, verbose_name='type_chinese')),
                ('type_english', models.CharField(max_length=80, verbose_name='type_english')),
                ('icp_number', models.CharField(max_length=20, verbose_name='icp_number')),
                ('icp_url', models.CharField(max_length=50, verbose_name='icp_url')),
                ('site_mail', models.CharField(max_length=50, verbose_name='site_mail')),
                ('site_qq', models.CharField(max_length=50, verbose_name='site_qq')),
                ('site_avatar', models.CharField(default='https://image.3001.net/images/20171226/15142933784705.png', max_length=200, verbose_name='site_avatar')),
            ],
            options={
                'verbose_name': 'site',
                'verbose_name_plural': 'site',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tag',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('username', models.CharField(blank=True, max_length=30, null=True, verbose_name='username')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='add_time')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='article')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment', verbose_name='pid')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comment',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='tag'),
        ),
    ]
