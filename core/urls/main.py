from django.urls import path, include
from core.views import main


app_name = 'core'
urlpatterns = [
    path('', main.IndexView.as_view(), name='index'),
    path('', include('core.urls.crud_urls')),
]
