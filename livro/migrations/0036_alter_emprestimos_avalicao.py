# Generated by Django 5.1.3 on 2024-12-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0035_alter_emprestimos_avalicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='avalicao',
            field=models.CharField(blank=True, choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo'), ('E', 'Excelente')], max_length=1, null=True),
        ),
    ]
