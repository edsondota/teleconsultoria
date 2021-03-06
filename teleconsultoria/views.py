import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from teleconsultoria.models import Teleconsultor, Solicitante, Teleconsultoria


class LoginView(View):
    def get(self, request):
        return render(request, 'teleconsultoria/login.html', locals())

    def post(self, request):
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active and user.is_superuser:
                login(request, user)
                return redirect('painel_view')
        messages.error(request, 'Não foi possível realizar seu login')
        return redirect('login_view')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_view')


class BaseAdminView(View):
    def dispatch(self, *args, **kwargs):
        request = self.request
        if not request.user.is_superuser:
            messages.error(request, 'Você não tem acesso a esta função')
            return redirect('logout_view')
        return super(BaseAdminView, self).dispatch(*args, **kwargs)


class BaseSolicitanteView(View):
    def dispatch(self, *args, **kwargs):
        request = self.request
        if not request.user.solicitante:
            messages.error(request, 'Você não tem acesso a esta função')
            return redirect('logout_view')
        return super(BaseSolicitanteView, self).dispatch(*args, **kwargs)


class BaseTeleconsultorView(View):
    def dispatch(self, *args, **kwargs):
        request = self.request
        if not request.user.teleconsultor:
            messages.error(request, 'Você não tem acesso a esta função')
            return redirect('logout_view')
        return super(BaseTeleconsultorView, self).dispatch(*args, **kwargs)


class PainelAdminView(BaseAdminView):
    def get(self, request):
        return render(request, 'teleconsultoria/painel_admin.html', locals())


class GerenciarTeleconsultorView(BaseAdminView):
    def get(self, request):
        teleconsultores = Teleconsultor.objects.all()
        return render(request, 'teleconsultoria/gerenciar_teleconsultor.html', locals())


class AdicionarTeleconsultorView(BaseAdminView):
    def get(self, request):
        return render(request, 'teleconsultoria/adicionar_teleconsultor.html', locals())

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        nome = request.POST['nome']
        crm = request.POST['crm']
        data_formatura = datetime.datetime.strptime(request.POST['data_formatura'], '%Y-%m-%d')
        usuario = None
        try:
            usuario = User.objects.create_user(
                    username=username, password=password, email=email)
            teleconsultor = Teleconsultor.objects.create(
                user = usuario,
                nome = nome,
                crm = crm,
                data_formatura = data_formatura
            )
        except:
            if usuario:
                usuario.delete()
            messages.error(request, u'Não foi possível cadastrar o Teleconsultor')
            return redirect('adicionar_teleconsultor_view')
        messages.success(request, u'Teleconsultor cadastrado com sucesso')
        return redirect('gerenciar_teleconsultor_view')


class EditarTeleconsultorView(BaseAdminView):
    def get(self, request):
        try:
            teleconsultor = Teleconsultor.objects.get(id=request.GET['id'])
        except:
            messages.error(request, u'O Teleconsultor não foi encontrado')
            return redirect('gerenciar_teleconsultor_view')
        return render(request, 'teleconsultoria/editar_teleconsultor.html', locals())

    def post(self, request):
        teleconsultor = None
        try:
            teleconsultor = Teleconsultor.objects.get(id=request.POST['id'])
        except:
            messages.error(request, u'O Teleconsultor não foi encontrado')
            return redirect('gerenciar_teleconsultor_view')
        username = request.POST['username']
        email = request.POST['email']
        nome = request.POST['nome']
        crm = request.POST['crm']
        data_formatura = datetime.datetime.strptime(request.POST['data_formatura'], '%Y-%m-%d')
        try:
            teleconsultor.user.username = username
            teleconsultor.user.email = email
            teleconsultor.nome = nome
            teleconsultor.crm = crm
            teleconsultor.data_formatura = data_formatura
            teleconsultor.user.save()
            teleconsultor.save()
        except:
            messages.error(request, u'Não foi possível editar o Teleconsultor')
            return redirect('editar_teleconsultor_view')
        messages.success(request, u'Teleconsultor alterado com sucesso')
        return redirect('gerenciar_teleconsultor_view')


class ApagarTeleconsultorView(BaseAdminView):
    def post(self, request):
        try:
            teleconsultor = Teleconsultor.objects.get(id=request.POST['id'])
            teleconsultor.user.delete()
            teleconsultor.delete()
            messages.success(request, u'Teleconsultor excluído com sucesso')
            return redirect('gerenciar_teleconsultor_view')
        except:
            messages.error(request, u'Não foi possível apagar o teleconsultor. Teleconsultor não encontrado')
            return redirect('gerenciar_teleconsultor_view')


class GerenciarSolicitanteView(BaseAdminView):
    def get(self, request):
        solicitantes = Solicitante.objects.all()
        return render(request, 'teleconsultoria/gerenciar_solicitante.html', locals())


class AdicionarSolicitanteView(BaseAdminView):
    def get(self, request):
        return render(request, 'teleconsultoria/adicionar_solicitante.html', locals())

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        usuario = None
        try:
            usuario = User.objects.create_user(
                    username=username, password=password, email=email)
            solicitante = Solicitante.objects.create(
                    user = usuario,
                    nome = nome,
                    telefone = telefone,
                    cpf = cpf,
            )
        except:
            if usuario:
                usuario.delete()
            messages.error(request, u'Não foi possível cadastrar o Solicitante')
            return redirect('adicionar_solicitante_view')
        messages.success(request, u'Solicitante cadastrado com sucesso')
        return redirect('gerenciar_solicitante_view')


class EditarSolicitanteView(BaseAdminView):
    def get(self, request):
        try:
            solicitante = Solicitante.objects.get(id=request.GET['id'])
        except:
            messages.error(request, u'O Solicitante não foi encontrado')
            return redirect('gerenciar_solicitante_view')
        return render(request, 'teleconsultoria/editar_solicitante.html', locals())

    def post(self, request):
        solicitante = None
        try:
            solicitante = Solicitante.objects.get(id=request.POST['id'])
        except:
            messages.error(request, u'O Solicitante não foi encontrado')
            return redirect('gerenciar_solicitante_view')
        username = request.POST['username']
        email = request.POST['email']
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        try:
            solicitante.user.username = username
            solicitante.user.email = email
            solicitante.nome = nome
            solicitante.cpf = cpf
            solicitante.telefone =telefone 
            solicitante.user.save()
            solicitante.save()
        except:
            messages.error(request, u'Não foi possível editar o Solicitante')
            return redirect('editar_solicitante_view')
        messages.success(request, u'Solicitante alterado com sucesso')
        return redirect('gerenciar_solicitante_view')


class ApagarSolicitanteView(BaseAdminView):
    def post(self, request):
        try:
            solicitante = Solicitante.objects.get(id=request.POST['id'])
            solicitante.user.delete()
            solicitante.delete()
            messages.success(request, u'Solicitante excluído com sucesso')
            return redirect('gerenciar_solicitante_view')
        except:
            messages.error(request, u'Não foi possível apagar o solicitante. Solicitante não encontrado')
            return redirect('gerenciar_solicitante_view')


class LoginSolicitanteView(View):
    def get(self, request):
        return render(request, 'teleconsultoria/login_solicitante.html', locals())

    def post(self, request):
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active and user.solicitante:
                login(request, user)
                return redirect('painel_solicitante_view')
        messages.error(request, 'Não foi possível realizar seu login')
        return redirect('login_solicitante_view')


class PainelSolicitanteView(BaseSolicitanteView):
    def get(self, request):
        teleconsultorias = Teleconsultoria.objects.filter(solicitante=request.user.solicitante)
        solicitante = request.user.solicitante
        return render(request, 'teleconsultoria/painel_solicitante.html', locals())


class AdicionarTeleconsultoriaView(BaseSolicitanteView):
    def get(self, request):
        if request.user.solicitante.pode_criar_teleconsultoria:
            teleconsultores = Teleconsultor.objects.all()
            return render(request, 'teleconsultoria/adicionar_teleconsultoria.html', locals())
        messages.error(request, 'Você não pode criar teleconsultorias por hoje')
        return redirect('painel_solicitante_view')

    def post(self, request):
        teleconsultor = None
        try:
            teleconsultor = Teleconsultor.objects.get(id=request.POST['teleconsultor'])
        except:
            messages.error(request, 'Não foi encontrado o teleconsultor informado')
            return redirect('adicionar_teleconsultoria_view')
        agendamento_teleconsultoria = datetime.datetime.strptime(request.POST['agendamento_teleconsultoria'], '%Y-%m-%dT%H:%M')
        texto = request.POST['texto']
        try:
            teleconsultoria = Teleconsultoria.objects.create(solicitante=request.user.solicitante,
                    teleconsultor=teleconsultor,
                    agendamento_teleconsultoria=agendamento_teleconsultoria,
                    texto=texto)
            messages.success(request, u'Teleconsultoria cadastrada com sucesso')
            return redirect('painel_solicitante_view')
        except:
            messages.error(request, 'Ocorreu um erro ao salvar a teleconsultoria')
            return redirect('adicionar_teleconsultoria_view')


class LoginTeleconsultorView(View):
    def get(self, request):
        return render(request, 'teleconsultoria/login_teleconsultor.html', locals())

    def post(self, request):
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active and user.teleconsultor:
                login(request, user)
                return redirect('painel_teleconsultor_view')
        messages.error(request, 'Não foi possível realizar seu login')
        return redirect('login_teleconsultor_view')


class PainelTeleconsultorView(BaseTeleconsultorView):
    def get(self, request):
        teleconsultorias = Teleconsultoria.objects.filter(teleconsultor=request.user.teleconsultor)
        teleconsultor = request.user.teleconsultor
        return render(request, 'teleconsultoria/painel_teleconsultor.html', locals())

class AceitarTeleconsultoriaView(BaseTeleconsultorView):
    def post(self, request):
        teleconsultoria = None
        try:
            teleconsultoria = Teleconsultoria.objects.get(id=request.POST['id'])
        except:
            messages.error(request, 'Não foi possível encontrar a teleconsultoria')
            return redirect('painel_teleconsultor_view')
        teleconsultoria.status_teleconsultoria = Teleconsultoria.ACEITA
        teleconsultoria.save()
        messages.success(request, 'Teleconsultoria aceita')
        return redirect('painel_teleconsultor_view')


class CancelarTeleconsultoriaView(BaseTeleconsultorView):
    def post(self, request):
        teleconsultoria = None
        try:
            teleconsultoria = Teleconsultoria.objects.get(id=request.POST['id'])
        except:
            messages.error(request, 'Não foi possível encontrar a teleconsultoria')
            return redirect('painel_teleconsultor_view')
        teleconsultoria.status_teleconsultoria = Teleconsultoria.CANCELADO
        teleconsultoria.save()
        messages.success(request, 'Teleconsultoria cancelada')
        return redirect('painel_teleconsultor_view')

