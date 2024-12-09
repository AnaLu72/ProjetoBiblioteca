from django.urls import path #importar o path do django
from . import views #significa que é do mesmo diretório, ou seja, do próprio diretório utilizadores

urlpatterns = [
    path('login/', views.login, name = 'login'), # o views.login é o nome da função que está no views.py
    path('registo/', views.registo, name = 'registo'),
    path('validar_registo/', views.validar_registo, name = 'validar_registo'),
    path('validar_login/', views.validar_login, name = 'validar_login'),
    path('logout/', views.logout, name = 'logout'),
]