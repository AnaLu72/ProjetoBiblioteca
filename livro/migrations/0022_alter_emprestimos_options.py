# Generated by Django 5.1.3 on 2024-11-18 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0021_remove_emprestimos_tempo_duracao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimos',
            options={'verbose_name': 'Emprestimos'},
        ),
    ]
