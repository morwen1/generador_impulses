from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, View
# Models
from Apps.General.user.models import Administrador, Cliente, Analista


class Index(TemplateView):
    template_name = 'index.html'


class Login(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if Administrador.objects.filter(usuario=user).exists():
                login(request, user)
                return redirect('admin:index')
            elif Cliente.objects.filter(usuario=user).exists():
                login(request, user)
                return redirect('cliente:index')
            elif Analista.objects.filter(usuario=user).exists():
                login(request, user)
                return redirect('analista:index')
            else:
                return render(request, self.template_name, {'error': 'No posees acceso'})
        else:
            return render(request, self.template_name, {'error': 'Credenciales inválidas'})


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')

