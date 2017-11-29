from backend.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','url', 'username','email','password','is_staff')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('id', 'nome', 'uf')

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ('id','nome','estado')

class EnderecoSerializer(serializers.ModelSerializer):
    cidade = CidadeSerializer()
    class Meta:
        model = Endereco
        fields = ('id','cep','tipo','logradouro','complemento','bairro','cidade')

    def create(self, validated_data):
        cidade_data = validated_data.pop('cidade')
        endereco = Endereco.objects.create(**validated_data)
        Cidade.objects.create(endereco=endereco, **cidade_data)
        return endereco

class PessoaSeralizer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    usuario = UserSerializer()
    class Meta:
        model = Pessoa
        fields = ('id','nome', 'sexo','dataNascimento','endereco','imagem','usuario')

class PessoaFisicaSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    usuario = UserSerializer()
    class Meta:
        model = PessoaFisica
        fields = ('id','cpf','nome','sexo','dataNascimento','endereco','imagem','usuario')

    def update(self, instance, validated_data):
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.sexo = validated_data.get('sexo', instance.sexo)
        instance.dataNascimento = validated_data.get('dataNascimento', instance.dataNascimento)
        instance.endereco = validated_data.get('endereco', instance.endereco)
        instance.imagem = validated_data.get('imagem', instance.imagem)
        instance.usuario = validated_data.get('usuario', instance.usuario)
        instance.save()
        return instance

    def create(self, validated_data):
        Endereco.cidade = Cidade
        endereco_data = validated_data.pop('endereco')
        usuario_data = validated_data.pop('usuario')
        pessoafisica = PessoaFisica.objects.create(**validated_data)
        Endereco.objects.create(pessoaFisica=pessoafisica, **endereco_data)
        User.objects.create(pessoaFisica=pessoafisica, **usuario_data)
        return pessoafisica

class EventoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    realizador = PessoaFisicaSerializer()
    class Meta:
        model = Evento
        fields = ('id','nome','sigla','numero','ano','descricao','palavras_chave','realizador','endereco','data_inicio','data_fim')

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.sigla = validated_data.get('sigla', instance.sigla)
        instance.numero = validated_data.get('numero', instance.numero)
        instance.ano = validated_data.get('ano', instance.ano)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.palavras_chave = validated_data.get('palavras_chave', instance.palavras_chave)
        instance.realizador = validated_data.get('realizador', instance.objects.realizador)
        instance.endereco = validated_data.get('endereco', instance.objects.endereco)
        instance.data_inicio= validated_data.get('data_inicio', instance.data_inicio)
        instance.data_fim= validated_data.get('data_fim', instance.data_fim)
        instance.save()
        return instance

    def create(self, validated_data):
        Endereco.cidade = Cidade
        endereco_data = validated_data.pop('endereco')
        evento = Evento.objects.create(**validated_data)
        Endereco.objects.create(evento=evento, **endereco_data)
        return evento

class TicketSerializer(serializers.ModelSerializer):
    evento = EstadoSerializer()
    class Meta:
        model = Ticket
        fields = ('id','nome','descricao','preco','vagas','evento')

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.preco = validated_data.get('preco', instance.preco)
        instance.vagas = validated_data.get('vagas', instance.vagas)
        instance.evento = validated_data.get('evento', instance.evento)
        instance.save()
        return instance

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

class InscricaoSerializer(serializers.ModelSerializer):
    pessoaFisica = PessoaFisicaSerializer()
    ticket = TicketSerializer()
    evento = EventoSerializer()

    class Meta:
        model = Inscricao
        fields = ('id','data','pessoaFisica','ticket','evento')

    def update(self, instance, validated_data):
        instance.data = validated_data.get('data', instance.data)
        instance.pessoaFisica = validated_data.get('pessoaFisica', instance.pessoaFisica)
        instance.ticket = validated_data.get('ticket', instance.ticket)
        instance.evento = validated_data.get('data', instance.evento)
        instance.save()
        return instance

    def create(self, validated_data):
        return Inscricao.objects.create(**validated_data)