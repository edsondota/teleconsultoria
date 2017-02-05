from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from teleconsultoria.views import LoginView, LogoutView, PainelAdminView
from teleconsultoria.views import GerenciarTeleconsultorView, AdicionarTeleconsultorView
from teleconsultoria.views import EditarTeleconsultorView, ApagarTeleconsultorView
from teleconsultoria.views import GerenciarSolicitanteView

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
    url(r'paine/gerenciar-solicitantes$',
        login_required(GerenciarSolicitanteView.as_view()),
        name="gerenciar_solicitante_view"),
    url(r'^admin/', include(admin.site.urls)),
]
