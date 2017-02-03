from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from teleconsultoria.views import LoginView, PainelAdminView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login_view"),
    url(r'^painel/administracao$', 
        login_required(PainelAdminView.as_view()), name="painel_view"),
    url(r'^admin/', include(admin.site.urls)),
]
