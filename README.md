# Upload_Projeto_Emprego
# Projeto-Quadro-de-Emprego
Sistema de Quadro de Vagas

## Criando o ambiente virtual
Criando seu ambiente virtual. Vamos chamá-lo de generic myvenv


```python
 -m venv myvenv
```
Ative o ambiente virtual 

```python
.myvenv\Scripts\activate bat .
```

Instalar o framework Django:


```python
pip install django
```
## Criando o projeto Django Emprego
```python
django-admin startproject emprego .
```
### Mudando as configurações
fazendo alterações algumas em emprego/settings.py. 

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
# Criando uma aplicação
```python
python manage.py startapp emprego
```
Depois de criar uma aplicação, também precisamos dizer ao Django que ele deve usá-la. Fazemos isso no arquivo core/settings.py -- abra-o no seu editor de código. Precisamos encontrar o INSTALLED_APPS e adicionar uma linha com 'pousada', logo acima do ].


```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'emprego',
]
```
### models emprego

```python
from django.db import models
from django.conf import settings


class Empresa(models.Model):
        nome_empresa = models.CharField(max_length=200)
        imagem_empresa = models.ImageField(upload_to='emprego/media', blank=True)
        descricao_empresa = models.TextField(max_length=200)
        cargo_oferecido = models.TextField(max_length=50)
        descricao_cargo = models.TextField(max_length=100)
        cidade_cargo = models.TextField(max_length=50)
        salario_oferecido = models.TextField()
        data_inicio = models.TextField(max_length = 20)
        data_encerramento = models.TextField(max_length = 20)
    

        def __str__(self):

                return self.nome_empresa 


class Usuario(models.Model):
        nome_usuario = models.CharField(max_length=200)
        cpf_usuario = models.TextField(max_length=15)
        telefone_usuario = models.TextField(max_length=15)
        cidade_usuario = models.TextField(max_length=100)
        bairro_usuario = models.TextField(max_length=100)
        rua_usuario = models.TextField(max_length=100)
        numero_usuario = models.TextField(max_length=10)
        email_usuario = models.TextField(max_length=50)
        senha_usuario = models.TextField(max_length=10)
        
    

        def __str__(self):
                return self.nome_usuario

class Candidato(models.Model):
        empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa")  
        usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario") 
    

        def __str__(self):
                return self.usuario
```
## Criando tabelas no banco de dados

Depois de criar os models , criamos as tabelas no banco.


```python
python manage.py makemigrations emprego
```

```python
python manage.py migrate emprego
```
## Django Admin

Alterações feitas no django admin.
```python
from django.contrib import admin
from .models import Usuario, Empresa, Candidato

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Candidato)
```
##criando um super usuário:

```python
python manage.py createsuperuser
```
```python
http://127.0.0.1:8000/admin/
```
```python
"""core URL Configuration

[...]
"""
rom django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emprego.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
```
##A URL do admin:

```python
path('admin/', admin.site.urls),
```
##Urls emprego (emprego/urls.py)

Todas a urls necessária para acessar nossas funções, e rotas do nosso sistema. Inclusive do login e logout .

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empresas, name='listar_empresas'),
    path('listar_empresas_area', views.listar_empresas_area, name='listar_empresas_area'),
    path('listar_candidato', views.listar_candidato, name='listar_candidato'),
    path('cadastrar_empresa', views.cadastrar_empresa, name='cadastrar_empresa'), 
    path('cadastrar_usuario', views.cadastrar_usuario, name='cadastrar_usuario'), 
    path('cadastrar_candidato', views.cadastrar_candidato, name='cadastrar_candidato'), 
    path('emprego/editar_empresa/<int:id>/', views.editar_empresa, name='editar_empresa'),
    path('emprego/editar_usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('emprego/<int:id>/', views.deletar_candidato, name='deletar_candidato'),
    path('emprego/editar_candidato/<int:id>/', views.editar_candidato, name='editar_candidato'),
    path('buscar_emprego', views.buscar_emprego, name='buscar_emprego'),
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
    path('emprego/<int:id>/', views.detalhar_candidato, name='detalhar_candidato'),
    path('emprego/<int:id>/', views.detalhar_empresa, name='detalhar_empresa'),
]

```
## views (emprego) 
Na views encontramos todas nossas Query set, que busca, edita, deleta e cadastra.

```python
from django.shortcuts import render, get_object_or_404, redirect
from emprego.models import Usuario, Empresa,  Candidato
import imghdr 
from emprego.forms import EmpresaForm
from emprego.forms import UsuarioForm
from emprego.forms import CandidatoForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def cadastrar_empresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            empresa = form.save(commit=False)
            img = request.FILES
            dados_img = imghdr.what(img['imagem_empresa'])
            if dados_img == 'png' or dados_img == 'jpeg':
                form.save()
                #return redirect('detalhar_livro', id=livro.id)
            else:
                 form = EmpresaForm()
                 return render(request, 'emprego/editar_emprego.html', {'form': form})             
    else:
        form = EmpresaForm()
        return render(request, 'emprego/editar_emprego.html', {'form': form})

def cadastrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save(commit=False)
            form.save()
            return render(request, 'emprego/login.html',{'form': form})

        

    else:
        form = UsuarioForm()
        return render(request, 'emprego/editar_usuario.html', {'form': form})

def cadastrar_candidato(request):
    if request.method == "POST":
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save(commit=False)
            form.save()
            return render(request, 'emprego/area_usuario.html', {'form': form})


        

    else:
        form = CandidatoForm()
        return render(request, 'emprego/editar_candidato.html', {'form': form})


def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            form.save()
            #return redirect('emprego/listar_emprego.html', id=empresa.id)
    else:
        form = UsuarioForm(instance=empresa)
        return render(request, 'emprego/editar_usuario.html', {'form': form})

def editar_empresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    if request.method == "POST":
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            empresa = form.save(commit=False)
            form.save()
            return redirect('emprego/listar_emprego.html', id=empresa.id)
    else:
        form = EmpresaForm(instance=empresa)
        return render(request, 'emprego/editar_emprego.html', {'form': form})

def editar_candidato(request, id):
    candidato = get_object_or_404(Candidato, pk=id)
    if request.method == "POST":
        form = CandidatoForm(request.POST, request.FILES, instance=candidato)
        if form.is_valid():
            candidato = form.save(commit=False)
            form.save()
            return render(request, 'emprego/area_usuario.html', {'form': form})
    else:
        form = CandidatoForm(instance=candidato)
        return render(request, 'emprego/editar_candidato.html', {'form': form})

def cadastrar_empresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            empresa = form.save(commit=False)
            img = request.FILES
            dados_img = imghdr.what(img['imagem_empresa'])
            if dados_img == 'png' or dados_img == 'jpeg':
                form.save()
                #return redirect('detalhar_livro', id=livro.id)
            else:
                 form = EmpresaForm()
                 return render(request, 'emprego/editar_emprego.html', {'form': form})             
    else:
        form = EmpresaForm()
        return render(request, 'emprego/editar_emprego.html', {'form': form})

def listar_empresas(request):
        empresas = Empresa.objects.all()
        return render(request, 'emprego/listar_emprego.html', {'empresas':empresas})

def listar_empresas_area(request):
        empresas = Empresa.objects.all()
        return render(request, 'emprego/listar_area_empresas.html', {'empresas':empresas})

def listar_candidato(request):
        candidatos = Candidato.objects.all()
        return render(request, 'emprego/listar_candidato.html', {'candidatos':candidatos})

def buscar_emprego(request):
    infor = request.POST['infor']
    empresas = Empresa.objects.filter(cargo_oferecido__contains=infor)
    return render(request, 'emprego/listar_emprego.html', {'empresas':empresas})

def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        usuarios = Usuario.objects.all()
        return render(request, 'emprego/area_usuario.html', {})
    else:
        return render(request, 'emprego/login.html',{})

def deletar_candidato(request, id):
    candidato = get_object_or_404(Candidato, pk=id)
    candidato.delete()
    return render(request, 'emprego/area_usuario.html', {'candidato':candidato})

def detalhar_candidato(request, id):
    candidato = get_object_or_404(Candidato, pk=id)
    return render(request, 'emprego/listar_candidato.html', {'candidato':candidato})

def detalhar_empresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    return render(request, 'emprego/listar_area_empresas.html', {'empresa':empresa})

def page_login(request):
    return render(request, 'emprego/login.html',{})

def logout_usuario(request):
    logout(request)
    return render(request, 'emprego/login.html',{})
```
#criando templates do nosso emprego
No arquivo template/emprego/listar_emprego.html temos o seguinte codigo:
também fazemos uso da restrição para salvar apenas imagens do quarto no formato .png e .jpeg. Para isso vamos utilizar a biblioteca imgdr que ficará responsável por pegar o formato da imagem. 

```python
{% extends 'emprego/base.html' %}

{% block content %}
    <h3>Vagas de Emprego(s)</h3>
    <hr>
        {% for empresa in empresas %}
           
            <img height="150" width="300" src="{{ empresa.imagem_empresa.url }}"><br>
            <b>Nome Empresa:</b> {{ empresa.nome_empresa }}<br/>
            <b>Descrição Empresa:</b> <br/>{{ empresa.descricao_empresa }}<br>
            <b>Cargo Oferecido:</b> {{ empresa.cargo_oferecido }}<br>
            <b>Descrição Cargo:</b> <br>{{ empresa.descricao_cargo }}<br>
            <b>Cidade Cargo:</b> {{ empresa.cidade_cargo }}<br/>
            <b>Salário Oferecido:</b> {{ empresa.salario_oferecido }}<br>
            <b>Data Inicio:</b> {{ empresa.data_inicio }}<br/>
            <b>Data Encerramento:</b> {{ empresa.data_encerramento }}<br>
            <a <button class="button_esprestimo" href="{% url 'page_login' %}">Candidata-se</button></a>
            <hr> 
            
        {% endfor %}
{% endblock %}

```
###No arquivo template/emprego/editar_emprego.html, edita os dados  caso seja necessário uma alteração.
```python
{% extends 'emprego/base.html' %}

{% block content %}
    <h2>Novo Cadastro</h2>
    <form method="POST" class="table" enctype="multipart/form-data">
    {% csrf_token %}
        <div class="form-group">
            {{ form.as_p }}
         </div>
         <button class="button_esprestimo">Salvar</button>
    </form>
{% endblock %}
```
#Tamplate da página principal base.html
Na base.html temos o codigo base que prepara, organiza e embeleza nossa inicial listar_emprego.html e tambem links para acessarmos as outras páginas da nossa aplicação.
```python
{% load static %}

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.80.0">
    <title>vagas de emprego(s)</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/album/">

    

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="{% static 'bootstrap.min.css' %}">
    

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
     


      .button_esprestimo {
      background-color: green; /* Green */
      border: none;
      color: white;
      padding: 12px 25px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 15px;
      border-radius: 4px;
      widows: 25%;
      margin-top: 3px;
      }
      .button_esprestimo:hover{
        background-color: gray;
      }
      .d-flex{
        margin-top: 10px;
        margin-bottom: 10px;
      }
      
      .button_cadastro {
      background-color: green; /* Green */
      border: none;
      color: white;
      padding: 12px 25px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 15px;
      border-radius: 4px;
      widows: 25%;
      margin-top: 3px;
      }
      .button_cadastro:hover{
        background-color: gray;
      }
      
    </style>

    
  </head>
  <body>
    
<header>
  <div class="collapse bg-dark" id="navbarHeader">
    <div class="container">
      <div class="row">
        <div class="col-sm-8 col-md-7 py-4">
          <h4 class="text-white">Sobre</h4>
          <p class="text-muted">Busque Vagas de Emprego no Nosso Site.</p>
        </div>
        <div class="col-sm-4 offset-md-1 py-4">
          <h4 class="text-white">Usuário</h4>
          <ul class="list-unstyled">
            <a <button class="btn btn-outline-success" href="{% url 'page_login' %}"type="submit" >Usuário</button></a>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="navbar navbar-dark bg-dark shadow-sm">
    <div class="container">
      <a href="#" class="navbar-brand d-flex align-items-center">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2" viewBox="0 0 24 24"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/></svg>
        <strong>Vagas A_Empregos</strong>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    </div>
  </div>
</header>

  <form class="d-flex"  action="{% url 'buscar_emprego' %}" method="POST">
    {% csrf_token %}
      <input name="infor" class="form-control me-2" type="search" placeholder="pesquise cargo nome desejado...." aria-label="Search">
      <button class="btn btn-outline-success" type="submit">Pesquisar</button>
 </form>

<main>

  <div class="album py-5 bg-light">
    <div class="container">
      

     
            {% block content %}

            
            {% endblock %}

            
      </div>
  </div>
      

       
</main>

<footer class="text-muted py-5">
  <div class="container">
    
    <p class="mb-1">&copy;vagas A_Empregos 2021</p>
   
  </div>
</footer>


    <script  rel="stylesheet" src="{% static 'bootstrap.bundle.min.js' %}"></script>
      
  </body>
</html>

```
## Preparando nossos Formulários
 Formulários para adicionar e editar os dados casdastrados no nosso sistema. 

emprego/forms.py

```python
from django import forms
from emprego.models import Empresa
from emprego.models import Usuario
from emprego.models import Candidato

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = ('nome_empresa','imagem_empresa','descricao_empresa','cargo_oferecido','descricao_cargo', 
        'cidade_cargo', 'salario_oferecido', 'data_inicio', 'data_encerramento')

        widgets = {
            'nome_empresa': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':''}),
            'imagem_empresa': forms.FileInput(attrs={ 'class': 'form-control'}),
            'descricao_empresa': forms.Textarea(attrs={ 'class': 'form-control'}),
            'cargo_oferecido': forms.Select(attrs={ 'class': 'form-control'}),
            'descricao_cargo': forms.Textarea(attrs={ 'class': 'form-control'}),
            'cidade_cargo': forms.TextInput(attrs={ 'class': 'form-control'}),
            'salario_oferecido': forms.TextInput(attrs={ 'class': 'form-control'}),
            'data_inicio': forms.TextInput(attrs={ 'class': 'form-control'}),
            'data_encerramento': forms.TextInput(attrs={ 'class': 'form-control'}),
       }

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('nome_usuario','cpf_usuario','telefone_usuario','cidade_usuario','bairro_usuario', 
        'rua_usuario', 'numero_usuario', 'email_usuario', 'senha_usuario')

        widgets = {
            'nome_usuario': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':''}),
            'cpf_usuario': forms.TextInput(attrs={ 'class': 'form-control'}),
            'telefone_usuario': forms.TextInput(attrs={ 'class': 'form-control'}),
            'cidade_usuario': forms.TextInput(attrs={ 'class': 'form-control'}),
            'bairro_usuario': forms.TextInput(attrs={ 'class': 'form-control'}),
            'rua_usuario': forms.TextInput(attrs={ 'class': 'form-control'}),
            'numero_usuario': forms.TextInput(attrs={ 'class': 'form-control'}),
            'email_usuario': forms.TextInput(attrs={ 'class': 'form-control'}),
            'senha_usuario': forms.TextInput(attrs={ 'class': 'form-control'}),
        }

class CandidatoForm(forms.ModelForm):

    class Meta:
        model = Candidato
        fields = ('empresa','usuario')

        widgets = {
            'empresa': forms.Select(attrs={ 'class': 'form-control', 
                                            'placeholder':''}),
            'usuario': forms.Select(attrs={ 'class': 'form-control'}),
           
       }
```
## Login , logout e autenticar_usuario do Sistema Emprego
Funções de login ,logout na views.py

```python
from django.contrib.auth import authenticate, login, logout
def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        usuarios = Usuario.objects.all()
        return render(request, 'emprego/area_usuario.html', {})
    else:
        return render(request, 'emprego/login.html',{})
        
def page_login(request):
    return render(request, 'emprego/login.html',{})

def logout_usuario(request):
    logout(request)
    return render(request, 'emprego/login.html',{})

```
Template do login : Formulario login template/emprego/login.html
```python
{% extends 'emprego/base.html' %}
{% block content %}
    <form action="{% url 'autenticar_usuario' %}" method="post">
    {% csrf_token %}
    <center><h3>LOGIN DO USUÁRIO</h3></center>
        <div class="mb-3" >
            <label for="exampleInputEmail1" class="form-label">Username</label>
            <input name="username" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input name="password" type="password" class="form-control" id="exampleInputPassword1">
        </div>
    <button type="submit" class="btn btn-primary">Entrar</button>
    <a <button type="submit" href="{% url 'cadastrar_usuario' %}" class="btn btn-primary">Cadastra-se</button></a>
    </form>
{% endblock %}

```
### Inserindo segurança na nossa lista de emprego

Vamos começar com a edição do arquivo `emprego/templates/emprego/area_usuario.html`. Vamos colocar `if user.is_authenticated` que verificará se o usuário destá em autenticado em uma sessão no navegador. Abra-o no editor de código e deixe ele dessa forma:
```python
 {% block content %}
          {% if user.is_authenticated %}
              <h5>Seja Bem Vindo,  {{user.username}}</h5>
          {% else %}
              <p>Você precisa realiar o login</p>
          {% endif %}
      {% endblock %}
```
