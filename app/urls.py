from django.urls import path
from .views import IndexView, HistoricoView, CuriosidadeView, ReferenciaView, CaracteristicaView, RegraView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('historico/', HistoricoView.as_view(), name='historico'),
    path('curiosidades/', CuriosidadeView.as_view(), name='curiosidade'),
    path('caracteristicas/', CaracteristicaView.as_view(), name='caracteristica'),
    path('referencias/', ReferenciaView.as_view(), name='referencia'),
    path('regras/', RegraView.as_view(), name='regra'),








]
