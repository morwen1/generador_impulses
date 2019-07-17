from django.views.generic import TemplateView
# Models
from Apps.General.licencia.models import LicenciaCliente


class Index(TemplateView):
    template_name = 'cliente/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        if 'licencias' not in context:
            context['licencias'] = LicenciaCliente.objects.filter(cliente=self.request.user.cliente)
        return context


