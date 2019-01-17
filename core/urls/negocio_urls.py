from django.urls import path, include
from core.views import negocio_views


app_name = 'core'
urlpatterns = [
    path('', negocio_views.IndexView.as_view(), name='index'),
    path('', include('core.urls.crud_urls')),
]
