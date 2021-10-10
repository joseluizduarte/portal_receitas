# Generated by Django 3.2.7 on 2021-10-09 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('receita_comentario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receitas.receita')),
            ],
        ),
    ]
