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
