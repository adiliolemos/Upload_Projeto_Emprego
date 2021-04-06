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