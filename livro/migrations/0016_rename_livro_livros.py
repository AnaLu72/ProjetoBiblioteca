# Generated by Django 5.1.3 on 2024-11-18 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0015_rename_livros_livro'),
        ('utilizadores', '0004_alter_utilizador_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Livro',
            new_name='Livros',
        ),
    ]