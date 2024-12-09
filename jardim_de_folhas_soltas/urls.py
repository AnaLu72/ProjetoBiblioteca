from django.contrib import admin
from django.urls import path, include #importar o include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), #incluir as rotas do admin
    path('auth/', include('utilizadores.urls')), #incluir as rotas do app utilizadores
    path('livro/', include('livro.urls')), #incluir as rotas do app livro
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)