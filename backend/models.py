from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField('nome', max_length=50)
    email = models.EmailField('email',max_length=50)
    senha = models.CharField('senha',max_length=30)


class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=100)
    sexo = models.CharField('sexo', max_length=1)
    dataNascimento = models.DateField()
    idEndereco = models.IntegerField()
    imagem = models.ImageField()
    idUsuario =  models.IntegerField

class PessoaFisica(models.Model):
    cpf = models.CharField('cpf', max_length=14)
    nome = models.CharField('nome', max_length=100)
    sexo = models.CharField('sexo', max_length=1)
    dataNascimento = models.DateField()
    idEndereco = models.IntegerField()
    imagem = models.ImageField()
    idUsuario = models.IntegerField

class Endereco(models.Model):
    cep = models.IntegerField('cep', max_length=8)
    tipo = models.charField('tipo', max_length=20)
    logradouro = models.charFiel('logradouro', max_length=50)
    complemento = models.charField('complemento', max_length=100)
    bairro = models.charField('bairro', max_length=50)
    idCidade = models.IntegerField()

class Cidade(models.Model):
    nome = models.CharField('nome', max_length=50)
    idEstado = models.IntegerField()

class Estado(models.Model):
    nome = models.CharField('nome', max_length=50)
    uf = models.CharField('uf', max_length=2)

class Evento(models.Model):
    nome = models.CharField('nome', max_length=100)
    sigla = models.CharField('sigla', max_length=20)
    numero = models.IntegerField('numero', max_length=4)
    ano = models.IntegerField('ano', max_length=4)
    descricao = models.TextField()
    palavras_chave = models.CharField('palavras_chave', max_length=100)
    realizador = models.IntegerField()
    idEndereco = models.IntegerField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    tickets = models.IntegerField()

class Ticket(models.Model):
    nome = models.CharField('nome', max_length=100)
    descricao = models.TextField()
    preco = models.FloatField()
    vagas = models.IntegerField()

class Inscricao(models.Model):
    data = models.DateTimeField()
    pessoa = models.IntegerField()
    ticket = models.IntegerField()
    evento = models.IntegerField()



