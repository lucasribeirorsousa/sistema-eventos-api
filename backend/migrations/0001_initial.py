# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 22:51
from __future__ import unicode_literals

import backend.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField(max_length=8, verbose_name='cep')),
                ('tipo', models.CharField(max_length=20, verbose_name='tipo')),
                ('logradouro', models.CharField(max_length=50, verbose_name='logradouro')),
                ('complemento', models.CharField(max_length=100, verbose_name='complemento')),
                ('bairro', models.CharField(max_length=50, verbose_name='bairro')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('uf', models.CharField(max_length=2, verbose_name='uf')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('sigla', models.CharField(max_length=20, verbose_name='sigla')),
                ('numero', models.IntegerField(max_length=4, verbose_name='numero')),
                ('ano', models.IntegerField(max_length=4, verbose_name='ano')),
                ('descricao', models.TextField()),
                ('palavras_chave', models.CharField(max_length=100, verbose_name='palavras_chave')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('ticket', models.IntegerField(verbose_name=backend.models.Ticket)),
                ('evento', models.IntegerField(verbose_name=backend.models.Evento)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('sexo', models.CharField(max_length=1, verbose_name='sexo')),
                ('dataNascimento', models.DateField()),
                ('imagem', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('descricao', models.TextField()),
                ('preco', models.FloatField()),
                ('vagas', models.IntegerField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Pessoa')),
                ('cpf', models.CharField(max_length=14, verbose_name='cpf')),
            ],
            bases=('backend.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Endereco'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Pessoa'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Estado'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='pessoaFisica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.PessoaFisica'),
        ),
    ]
