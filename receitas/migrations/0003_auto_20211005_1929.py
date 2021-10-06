# Generated by Django 3.2.7 on 2021-10-05 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_remove_receita_preparo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preparo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem', models.IntegerField()),
                ('instrucao', models.TextField()),
                ('receita_preparo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receitas.receita')),
            ],
        ),
        migrations.DeleteModel(
            name='Instrucao',
        ),
    ]