from django.shortcuts import redirect
# Models
from Apps.General.user.models import Administrador, Cliente, Analista


class AdminPermissionMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        full_path = request.get_full_path()
        if full_path.startswith('/admin/'):
            if not request.user.is_authenticated or not get_user(request, Administrador):
                return redirect('login')
        elif full_path.startswith('/cliente/'):
            if not request.user.is_authenticated or not get_user(request, Cliente):
                return redirect('login')
        elif full_path.startswith('/analista/'):
            if not request.user.is_authenticated or not get_user(request, Analista):
                return redirect('login')

        response = self.get_response(request)
        return response


def get_user(request, model):
    if not request.user.is_authenticated:
        return False
    else:
        return model.objects.filter(usuario=request.user).exists()
