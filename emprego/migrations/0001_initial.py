# Generated by Django 3.1.7 on 2021-03-24 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=200)),
                ('cpf_usuario', models.TextField(max_length=15)),
                ('telefone_usuario', models.TextField(max_length=15)),
                ('cidade_usuario', models.TextField(max_length=100)),
                ('bairro_usuario', models.TextField(max_length=100)),
                ('rua_usuario', models.TextField(max_length=100)),
                ('numero_usuario', models.TextField(max_length=10)),
                ('email_usuario', models.TextField(max_length=50)),
                ('senha_usuario', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=200)),
                ('imagem_empresa', models.ImageField(blank=True, upload_to='livraria/media')),
                ('descricao_empresa', models.TextField(max_length=200)),
                ('cargo_oferecido', models.TextField(max_length=50)),
                ('descricao_cargo', models.TextField(max_length=100)),
                ('cidade_cargo', models.TextField(max_length=50)),
                ('salario_oferecido', models.FloatField()),
                ('data_inicio', models.TextField(max_length=20)),
                ('data_encerramento', models.TextField(max_length=20)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprego.usuario', verbose_name='Usuario')),
            ],
        ),
    ]