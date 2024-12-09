# Generated by Django 5.1.3 on 2024-11-18 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0017_remove_livros_genero_categoria_utilizador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_emprestimo',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='nome_emprestado',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='tempo_duracao',
        ),
        migrations.CreateModel(
            name='Empréstimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_emprestado', models.CharField(blank=True, max_length=50)),
                ('data_emprestimo', models.DateField(blank=True, null=True)),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('tempo_duracao', models.DateField(blank=True, null=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros')),
            ],
        ),
    ]