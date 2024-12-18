# Generated by Django 5.1.3 on 2024-11-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='co_autor',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='livros',
            name='emprestado_a',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='livros',
            name='emprestado_data',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='emprestado_data_devolucao',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='emprestado_data_devolucao_real',
            field=models.DateField(blank=True),
        ),
    ]
