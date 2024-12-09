# Generated by Django 5.1.3 on 2024-11-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('co_autor', models.CharField(max_length=30)),
                ('data_registo', models.DateField()),
                ('emprestado', models.BooleanField(default=False)),
                ('emprestado_a', models.CharField(max_length=100)),
                ('emprestado_data', models.DateField()),
                ('emprestado_data_devolucao', models.DateField()),
                ('emprestado_data_devolucao_real', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
                ('editora', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('estado_leitura', models.CharField(choices=[('nao_lido', 'Não Lido'), ('a_ler', 'A Ler'), 
                                                             ('lido', 'Lido'), ('emprestado', 'Emprestado'), 
                                                             ('entregue', 'Entregue')], max_length=20)),
            ],
        ),
    ]