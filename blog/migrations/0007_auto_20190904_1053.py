# Generated by Django 2.0.13 on 2019-09-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190903_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='contenu_fr',
            field=models.TextField(db_column='art_contenu_fr', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='titre_fr',
            field=models.CharField(db_column='art_titre_fr', max_length=100, null=True),
        ),
    ]
