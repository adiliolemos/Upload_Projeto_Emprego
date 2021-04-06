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