# Generated by Django 5.1.3 on 2024-11-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_alter_livros_options_remove_livros_emprestado_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='genero',
            field=models.CharField(choices=[('ficcao', 'Ficção'), ('romance', 'Romance'), ('policial', 'Policial'), ('triller', 'Triller'), ('fantasia', 'Fantasia'), ('autoajuda', 'Autoajuda'), ('biografia', 'Biografia'), ('culinaria', 'Culinária'), ('outros', 'Outros')], max_length=50),
        ),
    ]
