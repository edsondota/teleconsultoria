from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View


class LoginView(View):
    def get(self, request):
        return render(request, 'teleconsultoria/login.html', locals())
