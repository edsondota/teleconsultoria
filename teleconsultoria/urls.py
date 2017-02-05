from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from teleconsultoria.views import LoginView, LogoutView, PainelAdminView
from teleconsultoria.views import GerenciarTeleconsultorView, AdicionarTeleconsultorView
from teleconsultoria.views import EditarTeleconsultorView, ApagarTeleconsultorView
from teleconsultoria.views import GerenciarSolicitanteView, AdicionarSolicitanteView
from teleconsultoria.views import EditarSolicitanteView, ApagarSolicitanteView
from teleconsultoria.views import LoginSolicitanteView, PainelSolicitanteView
from teleconsultoria.views import AdicionarTeleconsultoriaView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login_view"),
    url(r'^logout', LogoutView.as_view(), name="logout_view"),
    url(r'^painel/administracao$', 
        login_required(PainelAdminView.as_view()), name="painel_view"),
    url(r'^painel/gerenciar-teleconsultor$',
        login_required(GerenciarTeleconsultorView.as_view()),
        name="gerenciar_teleconsultor_view"),
    url(r'painel/adicionar-teleconsultor$',
        login_required(AdicionarTeleconsultorView.as_view()),
        name="adicionar_teleconsultor_view"),
    url(r'painel/editar-teleconsultor$',
        login_required(EditarTeleconsultorView.as_view()),
        name="editar_teleconsultor_view"),
    url(r'painel/apagar-teleconsultor$',
        login_required(ApagarTeleconsultorView.as_view()),
        name="apagar_teleconsultor_view"),
    url(r'painel/gerenciar-solicitantes$',
        login_required(GerenciarSolicitanteView.as_view()),
        name="gerenciar_solicitante_view"),
    url(r'painel/adicionar-solicitante$',
        login_required(AdicionarSolicitanteView.as_view()),
        name="adicionar_solicitante_view"),
    url(r'painel/editar-solicitante$',
        login_required(EditarSolicitanteView.as_view()),
        name="editar_solicitante_view"),
    url(r'painel/apagar-solicitante$',
        login_required(ApagarSolicitanteView.as_view()),
        name="apagar_solicitante_view"),
    url(r'login-solicitante$', LoginSolicitanteView.as_view(), name="login_solicitante_view"),
    url(r'solicitante/painel-solicitantes$',
        login_required(PainelSolicitanteView.as_view()),
        name="painel_solicitante_view"),
    url(r'solicitante/adicionar-teleconsultoria$',
        login_required(AdicionarTeleconsultoriaView.as_view()),
        name="adicionar_teleconsultoria_view"),
    url(r'^admin/', include(admin.site.urls)),
]
