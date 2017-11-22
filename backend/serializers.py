from backend.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url', 'username', 'email', 'is_staff')

class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('id', 'nome', 'uf')

class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = ('id', 'nome','estado')

class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = ('cep','tipo','logradouro','complemento','bairro','cidade')

class PessoaSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('nome', 'sexo','dataNascimento','endereco','imagem','usuario')

class PessoaFisicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PessoaFisica
        fields = ('cpf','nome', 'sexo','dataNascimento','endereco','imagem','usuario')

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('nome','sigla','numero','ano','descricao','palavras_chave','realizador','endereco','data_inicio','data_fim')

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('nome','descricao','preco','vagas','evento')

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inscricao
        fields = ('data','pessoaFisica','ticket','evento')