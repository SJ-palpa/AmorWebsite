# Generated by Django 2.0.13 on 2019-09-03 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190903_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='contenu_fr',
        ),
        migrations.RemoveField(
            model_name='article',
            name='titre_fr',
        ),
    ]