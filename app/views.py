from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
class HistoricoView(TemplateView):
    template_name = "historico.html"
class CuriosidadeView(TemplateView):
    template_name = "curiosidade.html"
class RegraView(TemplateView):
    template_name = "regra.html"
class ReferenciaView(TemplateView):
    template_name = "referencia.html"
class CaracteristicaView(TemplateView):
    template_name = "caracteristica.html"