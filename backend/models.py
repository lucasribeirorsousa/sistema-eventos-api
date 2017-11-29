from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    nome = models.CharField('nome', max_length=50)
    uf = models.CharField('uf', max_length=2)

    def __str__(self):
        return self.nome
class Cidade(models.Model):
    nome = models.CharField('nome', max_length=50)
    estado = models.ForeignKey(Estado)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    cep = models.IntegerField('cep', max_length=8)
    tipo = models.CharField('tipo', max_length=20)
    logradouro = models.CharField('logradouro', max_length=50)
    complemento = models.CharField('complemento', max_length=100)
    bairro = models.CharField('bairro', max_length=50)
    cidade = models.ForeignKey(Cidade)

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=100)
    sexo = models.CharField('sexo', max_length=1)
    dataNascimento = models.DateField()
    endereco = models.ForeignKey(Endereco)
    imagem = models.ImageField()
    usuario = models.ForeignKey(User)

class PessoaFisica(Pessoa):
    cpf = models.CharField('cpf', max_length=14)

class Evento(models.Model):
    nome = models.CharField('nome', max_length=100)
    sigla = models.CharField('sigla', max_length=20)
    numero = models.IntegerField('numero', max_length=4)
    ano = models.IntegerField('ano', max_length=4)
    descricao = models.TextField()
    palavras_chave = models.CharField('palavras_chave', max_length=100)
    realizador = models.ForeignKey(Pessoa)
    endereco = models.ForeignKey(Endereco)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

class Ticket(models.Model):
    nome = models.CharField('nome', max_length=100)
    descricao = models.TextField()
    preco = models.FloatField()
    vagas = models.IntegerField()
    evento =  models.ForeignKey(Evento)

class Inscricao(models.Model):
    data = models.DateTimeField()
    pessoaFisica = models.ForeignKey(PessoaFisica)
    ticket = models.IntegerField(Ticket)
    evento = models.IntegerField(Evento)



