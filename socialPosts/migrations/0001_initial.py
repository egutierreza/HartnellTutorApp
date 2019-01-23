# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-18 23:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tutorApp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1600)),
                ('score', models.IntegerField(default=0)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('viewed', models.DateTimeField(blank=True, null=True)),
                ('action_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='socialPosts.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=1200)),
                ('score', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_type', models.CharField(default='', max_length=1)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='tutorApp.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=35)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField()),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='socialPosts.Comment')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='socialPosts.Post')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='tutorApp.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='socialPosts.Tag'),
        ),
        migrations.AddField(
            model_name='notification',
            name='action_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='socialPosts.Post'),
        ),
        migrations.AddField(
            model_name='notification',
            name='actor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifying', to='tutorApp.Profile'),
        ),
        migrations.AddField(
            model_name='notification',
            name='target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifier', to='tutorApp.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='socialPosts.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tutorApp.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='responses',
            field=models.ManyToManyField(blank=True, related_name='_comment_responses_+', to='socialPosts.Comment'),
        ),
    ]