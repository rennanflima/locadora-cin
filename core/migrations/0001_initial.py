# Generated by Django 2.1.5 on 2019-02-11 19:38

import core.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', core.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ArgumentoPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo', models.CharField(max_length=100, verbose_name='Nome do campo')),
                ('is_requerido', models.BooleanField(default=False, verbose_name='Campo obrigatório?')),
                ('tipo_dado', models.CharField(choices=[('TEXTO', 'Texto'), ('INTEIRO', 'Inteiro'), ('DECIMAL', 'Decimal'), ('BOOLEAN', 'Boolean'), ('DATA', 'Data'), ('HORA', 'Hora'), ('DATA_HORA', 'Data/Hora')], max_length=20, verbose_name='Tipo de dado do campo')),
            ],
            options={
                'verbose_name': 'Argumento do Pagamento',
                'verbose_name_plural': 'Argumentos dos Pagamentos',
            },
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, unique=True, verbose_name='Nome')),
                ('tipo', multiselectfield.db.fields.MultiSelectField(choices=[('Diretor', 'Diretor'), ('Ator', 'Ator')], max_length=12, verbose_name='Atividade')),
            ],
            options={
                'verbose_name': 'Artista',
                'verbose_name_plural': 'Artistas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('capital', models.BooleanField(default=False, verbose_name='Capital ?')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'ordering': ['estado__nome', 'nome'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=150, unique=True, verbose_name='Código')),
                ('local_trabalho', models.CharField(blank=True, max_length=150, null=True, verbose_name='Local de Trabalho')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this client should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('titular', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clientes', to='core.Cliente')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=150, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=20, verbose_name='CNPJ')),
                ('contato', models.CharField(max_length=150, verbose_name='Pessoa de Contato')),
                ('telefone', models.CharField(max_length=30, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Distribuidora',
                'verbose_name_plural': 'Distribuidoras',
                'ordering': ['razao_social'],
            },
        ),
        migrations.CreateModel(
            name='Elenco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personagem', models.CharField(blank=True, max_length=150, null=True, verbose_name='Personagem')),
                ('principal', models.BooleanField(default=False, verbose_name='Principal ?')),
                ('ator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Artista')),
            ],
            options={
                'verbose_name': 'Elenco',
                'verbose_name_plural': 'Elencos',
                'ordering': ['ator', 'principal'],
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100, verbose_name='Logradouro')),
                ('numero', models.PositiveIntegerField(verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=60, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Cidade')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
                'ordering': ['logradouro', 'numero', 'cidade'],
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, unique=True, verbose_name='Nome')),
                ('sigla', models.CharField(max_length=30, unique=True, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título em Português')),
                ('titulo_original', models.CharField(max_length=150, verbose_name='Título Original')),
                ('sinopse', models.TextField(verbose_name='Sinopse')),
                ('classificacao', models.CharField(choices=[('L', 'Livre'), ('10', '10 - Não recomendado para menores de 10 anos'), ('12', '12 - Não recomendado para menores de 12 anos'), ('14', '14 - Não recomendado para menores de 14 anos'), ('16', '16 - Não recomendado para menores de 16 anos'), ('18', '18 - Não recomendado para maiores de 18 anos')], max_length=2, verbose_name='Classificação Indicativa')),
                ('duracao', models.TimeField(verbose_name='Duração')),
                ('ano', models.PositiveSmallIntegerField(verbose_name='Ano de Lançamento')),
                ('pais', models.CharField(max_length=150, verbose_name='Nacionalidade')),
                ('capa', models.ImageField(blank=True, null=True, upload_to='capas/', verbose_name='Capa do Filme')),
                ('is_lancamento', models.BooleanField(default=False, help_text='Designa se este filme deve ser tratado como lançamento. Desmarque esta opção se não for um lançamento.', verbose_name='Lançamento')),
                ('diretor', models.ManyToManyField(to='core.Artista')),
                ('distribuidora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Distribuidora')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, unique=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Forma de Pagamento',
                'verbose_name_plural': 'Formas de Pagamento',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Gênero',
                'verbose_name_plural': 'Gêneros',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='HistoricoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao_cliente', models.BooleanField(default=True, verbose_name='Situação do Cliente')),
                ('data_alteracao', models.DateTimeField(auto_now_add=True, verbose_name='update date')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='historico_cliente', to='core.Cliente')),
                ('titular', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='historico_dependente', to='core.Cliente')),
            ],
            options={
                'verbose_name': 'Histórico do Cliente',
                'verbose_name_plural': 'Históricos dos Clientes',
                'ordering': ['data_alteracao'],
            },
        ),
        migrations.CreateModel(
            name='InformacaoPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_texto', models.TextField(blank=True, null=True, verbose_name='Valor da informação em Texto')),
                ('valor_inteiro', models.IntegerField(blank=True, null=True, verbose_name='Valor da informação em Número Inteiro')),
                ('valor_decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor da informação em Número Decimal')),
                ('valor_data', models.DateField(blank=True, null=True, verbose_name='Valor da informação em Data')),
                ('valor_hora', models.TimeField(blank=True, null=True, verbose_name='Valor da informação em Hora')),
                ('valor_data_hora', models.DateTimeField(blank=True, null=True, verbose_name='Valor da informação em Data/Hora')),
                ('valor_boolean', models.BooleanField(blank=True, null=True, verbose_name='Valor da informação Verdadeiro ou Falso')),
                ('argumento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='informacoes_argumentos', to='core.ArgumentoPagamento')),
            ],
            options={
                'verbose_name': 'Informação do Pagamento',
                'verbose_name_plural': 'Informações dos Pagamentos',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_serie', models.CharField(max_length=150, verbose_name='Número de Série')),
                ('data_aquisicao', models.DateField(verbose_name='Data de Aquisição')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Número de Cópias')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this item should be treated as active. Unselect this instead of deleting items.', verbose_name='active')),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itens_filme', related_query_name='item_filme', to='core.Filme')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
                'ordering': ['data_aquisicao'],
            },
        ),
        migrations.CreateModel(
            name='ItemLocacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_lancamento', models.BooleanField(default=False, help_text='Designa se este filme deve ser tratado como lançamento. Desmarque esta opção se não for um lançamento.', verbose_name='Lançamento')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Valor da Locação')),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Desconto da Locação')),
                ('data_devolucao_prevista', models.DateField(blank=True, null=True, verbose_name='Data de Devolução Prevista')),
                ('nova_data_devolucao', models.DateField(blank=True, null=True, verbose_name='Nova Data de Devolução')),
            ],
            options={
                'verbose_name': 'Item de Locação',
                'verbose_name_plural': 'Itens de Locação',
            },
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Sub-Total da Locação')),
                ('total_descontos', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Valor Total de Descontos')),
                ('valor_total', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Valor Total da Locação')),
                ('data_locacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Locação')),
                ('situacao', models.CharField(choices=[('EM_ANDAMENTO', 'Em Andamento'), ('CONCLUIDA', 'Concluída'), ('PAGA', 'Paga'), ('PAGA_PARCIAL', 'Paga Parcialmente'), ('CANCELADA', 'Cancelada')], default='EM_ANDAMENTO', max_length=20, verbose_name='Situação da Locação')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Cliente')),
            ],
            options={
                'verbose_name': 'Locação',
                'verbose_name_plural': 'Locações',
                'ordering': ['data_locacao'],
            },
        ),
        migrations.CreateModel(
            name='Midia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Valor da Locação')),
            ],
            options={
                'verbose_name': 'Tipo de Mídia',
                'verbose_name_plural': 'Tipos de Mídias',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pagamento', models.DateTimeField(auto_now_add=True, verbose_name='Data de Pagamento')),
                ('forma_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.FormaPagamento')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='CPF')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=2, verbose_name='Sexo')),
                ('endereco', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Endereco')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateTimeField(auto_now_add=True, verbose_name='booking date')),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Expirada', 'Expirada'), ('Atendida', 'Atendida')], default='Pendente', max_length=10, verbose_name='Situação da Reserva')),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.Cliente')),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservas_filme', related_query_name='reserva', to='core.Filme')),
                ('midia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reservas_midia', related_query_name='reserva', to='core.Midia')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reserva',
                'ordering': ['data_reserva'],
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=30, verbose_name='Número')),
                ('tipo', models.CharField(choices=[('Residencial', 'Residencial'), ('Trabalho', 'Trabalho'), ('Celular', 'Celular'), ('Outro', 'Outro')], max_length=15, verbose_name='Tipo de Telefone')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Perfil')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Devolucao',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='core.ItemLocacao')),
                ('data_devolucao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Devolução')),
                ('multa', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True, verbose_name='Multa por Atraso')),
            ],
            options={
                'verbose_name': 'Devolução',
                'verbose_name_plural': 'Devoluções',
            },
        ),
        migrations.AddField(
            model_name='itemlocacao',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Item'),
        ),
        migrations.AddField(
            model_name='itemlocacao',
            name='locacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Locacao'),
        ),
        migrations.AddField(
            model_name='itemlocacao',
            name='pagamentos',
            field=models.ManyToManyField(to='core.Pagamento'),
        ),
        migrations.AddField(
            model_name='item',
            name='tipo_midia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itens_midia', related_query_name='item_midia', to='core.Midia'),
        ),
        migrations.AddField(
            model_name='informacaopagamento',
            name='pagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='informacoes_pagamentos', to='core.Pagamento'),
        ),
        migrations.AddField(
            model_name='filme',
            name='genero',
            field=models.ManyToManyField(to='core.Genero'),
        ),
        migrations.AlterUniqueTogether(
            name='estado',
            unique_together={('nome', 'sigla')},
        ),
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Estado'),
        ),
        migrations.AddField(
            model_name='elenco',
            name='filme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Filme'),
        ),
        migrations.AddField(
            model_name='distribuidora',
            name='endereco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Endereco'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Estado'),
        ),
        migrations.AddField(
            model_name='argumentopagamento',
            name='forma_pagamento',
            field=models.ManyToManyField(to='core.FormaPagamento'),
        ),
        migrations.AlterUniqueTogether(
            name='elenco',
            unique_together={('filme', 'ator')},
        ),
        migrations.AlterUniqueTogether(
            name='cidade',
            unique_together={('nome', 'estado')},
        ),
    ]
