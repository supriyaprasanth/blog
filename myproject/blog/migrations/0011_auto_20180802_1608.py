# Generated by Django 2.0.7 on 2018-08-02 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='author',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
