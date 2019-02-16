import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locadora.settings.development')

django.setup()

from core.models import User, Perfil

u = User.objects.create_superuser(
    email='teste@bdd.com', password='123456', first_name='teste', last_name="bdd"
)
u.save()

u.perfil.cpf =  cpf ="32808972032"
u.perfil.data_nascimento="2019-02-01"
u.perfil.sexo="F"
u.save()
