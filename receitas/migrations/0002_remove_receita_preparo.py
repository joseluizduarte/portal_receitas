# Generated by Django 3.2.7 on 2021-10-05 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='preparo',
        ),
    ]