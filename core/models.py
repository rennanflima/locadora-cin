from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from core.choices import *
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.managers import UserManager
from datetime import date
from django.conf import settings


# Create your models here.
class Role(models.Model):
    CLIENTE = 1
    FUNCIONARIO = 2
    ADMIN = 3
    SUPER_USER = 4
    ROLE_CHOICES = (
        (CLIENTE, 'Cliente'),
        (FUNCIONARIO, 'Funcionário'),
        (ADMIN, 'Admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    roles = models.ManyToManyField(Role)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Genero(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)

    class Meta:
        ordering = ['nome',]
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

    def __str__(self):
        return "%s" % self.nome 

    def get_absolute_url(self):
        return reverse('core:genero-detalhe', kwargs={'pk': self.pk})

class Artista(models.Model):
    nome = models.CharField('Nome', max_length=150, unique=True)
    tipo = MultiSelectField('Atividade', choices=tipo_pessoa_filme)

    class Meta:
        ordering = ['nome',]
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'

    def __str__(self):
        return "%s" % self.nome 

    def get_absolute_url(self):
        return reverse('core:artista-detalhe', kwargs={'pk': self.pk})

class Estado(models.Model):
    nome = models.CharField('Nome', max_length=60, unique=True)
    sigla = models.CharField('Sigla', max_length=30, unique=True)

    class Meta:
        ordering = ['nome',]
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return "%s" % self.nome

    def get_absolute_url(self):
        return reverse('core:estado-detalhe', kwargs={'pk': self.pk})
    
    def clean(self):
        self.nome = self.nome.lower().capitalize()
        self.sigla = self.sigla.upper()

class Cidade(models.Model):
    nome = models.CharField('Nome', max_length=60)
    capital = models.BooleanField('Capital ?', default=False)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    class Meta:
        ordering = ['nome', 'estado',]
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return "%s/%s" % (self.nome, self.estado.sigla)

    def get_absolute_url(self):
        return reverse('core:cidade-detalhe', kwargs={'pk': self.pk})

class Endereco(models.Model):
    logradouro = models.CharField('Logradouro', max_length=100)
    numero = models.PositiveIntegerField('Número')
    complemento = models.CharField('Complemento', max_length=60, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=50)
    cep = models.CharField('CEP', max_length=10)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    class Meta:
        ordering = ['logradouro', 'numero', 'cidade',]
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return "%s, nº %d - %s - %s - CEP %s" % (self.logradouro, self.numero, self.bairro, self.cidade, self.cep)

    def get_absolute_url(self):
        return reverse('core:endereco-detalhe', kwargs={'pk': self.pk})

class Distribuidora(models.Model):
    razao_social = models.CharField('Razão Social', max_length=150)
    cnpj = models.CharField('CNPJ', max_length=20)
    contato = models.CharField('Pessoa de Contato', max_length=150)
    telefone = models.CharField('Telefone', max_length=30)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    class Meta:
        ordering = ['razao_social',]
        verbose_name = 'Distribuidora'
        verbose_name_plural = 'Distribuidoras'

    def __str__(self):
        return "%s" % self.razao_social

    def get_absolute_url(self):
        return reverse('core:distribuidora-detalhe', kwargs={'pk': self.pk})

class Filme(models.Model):
    titulo = models.CharField('Título em Português', max_length=150) 
    titulo_original = models.CharField('Título Original', max_length=150)
    sinopse = models.TextField('Sinopse')
    classificacao = models.CharField('Classificação Indicativa', max_length=2, choices=tipo_classificacao)
    duracao = models.TimeField('Duração')
    diretor = models.ManyToManyField(Artista)
    ano = models.PositiveSmallIntegerField('Ano de Lançamento')
    pais = models.CharField('País', max_length=150)
    genero = models.ManyToManyField(Genero)
    distribuidora = models.ForeignKey(Distribuidora, on_delete=models.PROTECT)
    capa = models.ImageField('Capa do Filme', upload_to = 'capas/', blank=True, null=True)

    class Meta:
        ordering = ['titulo',]
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return "%s (%s)" % (self.titulo, self.titulo_original)
    
    def get_absolute_url(self):
        return reverse('core:filme-detalhe', kwargs={'pk': self.pk})

class Elenco(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ator =  models.ForeignKey(Artista, on_delete=models.CASCADE)
    personagem = models.CharField('Personagem', max_length=150, null=True, blank=True)
    principal = models.BooleanField('Principal ?', default=False)

    class Meta:
        unique_together = ('filme', 'ator')
        ordering = ['ator', 'principal',]
        verbose_name = 'Elenco'
        verbose_name_plural = 'Elencos'

    def __str__(self):
        return "%s (%s)" % (self.ator, self.personagem)

    def get_absolute_url(self):
        return reverse('core:elenco-detalhe', kwargs={'pk': self.pk})

    def clean(self):
        if self.ator and not self.personagem:
            raise ValidationError({'personagem': _("É obrigatório informar o nome do personagem para o ator: '%s'." % self.ator)})

class Midia(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    valor = models.DecimalField('Valor da Locação', max_digits=8, decimal_places=2, default=0)

    class Meta:
        ordering = ['nome',]
        verbose_name = 'Tipo de Mídia'
        verbose_name_plural = 'Tipos de Mídias'

    def __str__(self):
        return "%s" % self.nome

    def get_absolute_url(self):
        return reverse('core:midia-detalhe', kwargs={'pk': self.pk})

class Item(models.Model):
    numero_serie = models.CharField('Número de Série', max_length=150)
    data_aquisicao = models.DateField('Data de Aquisição')
    tipo_midia = models.ForeignKey(Midia, on_delete=models.PROTECT)
    filme = models.ForeignKey(Filme, on_delete=models.PROTECT)

    class Meta:
        ordering = ['data_aquisicao',]
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return "%s (%s)" % (self.filme, self.tipo_midia)

    def get_absolute_url(self):
        return reverse('core:item-detalhe', kwargs={'pk': self.pk})

class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=15, unique=True, blank=True, null=True)
    data_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)
    sexo = models.CharField('Sexo', max_length=2, choices=tipo_sexo)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        # ordering = ['data_aquisicao',]
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()

class Telefone(models.Model):
    numero = models.CharField('Número', max_length=30)
    tipo = models.CharField('Tipo de Telefone', max_length=15, choices=tipo_telefone)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    class Meta:
        ordering = ['tipo',]
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return "%s - %s" % (self.numero, self.tipo)

class Dependente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    codigo = models.CharField('Código', max_length=150, unique=True, default='0')
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this dependent should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    class Meta:
        ordering = ['codigo',]
        verbose_name = 'Dependente'
        verbose_name_plural = 'Dependentes'

    def __str__(self):
        return "%s" % (self.user.get_full_name())

    def get_absolute_url(self):
        return reverse('core:dependente-detalhe', kwargs={'pk': self.pk})

class Cliente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    codigo = models.CharField('Código', max_length=150, unique=True)
    local_trabalho = models.CharField('Local de Trabalho', max_length=150)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this client should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    dependentes = models.ManyToManyField(Dependente, related_name='clientes', related_query_name='cliente')

    class Meta:
        # ordering = ['data_aquisicao',]
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return "%s" % (self.user.get_full_name())

    def get_absolute_url(self):
        return reverse('core:cliente-detalhe', kwargs={'pk': self.pk})
    