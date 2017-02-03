import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from teleconsultoria.models import Teleconsultor, Solicitante


class LoginView(View):
    def get(self, request):
        return render(request, 'teleconsultoria/login.html', locals())

    def post(self, request):
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('painel_view')
        return redirect('login_view')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_view')


class PainelAdminView(View):
    def get(self, request):
        return render(request, 'teleconsultoria/painel_admin.html', locals())


class GerenciarTeleconsultorView(View):
    def get(self, request):
        teleconsultores = Teleconsultor.objects.all()
        return render(request, 'teleconsultoria/gerenciar_teleconsultor.html', locals())


class AdicionarTeleconsultorView(View):
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
            messages.error(request, u'Não foi possível cadastrar o Teleconsultor', extra_tags='danger')
            return redirect('adicionar_teleconsultor_view')
        return redirect('gerenciar_teleconsultor_view')
