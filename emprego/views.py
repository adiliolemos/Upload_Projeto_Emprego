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