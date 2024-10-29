from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'perfiles'

urlpatterns = [
    path('<uuid:pk>/', PerfilDetailView.as_view(), name='perfil-detail'),
    path('<uuid:pk>/editar/', PerfilUpdateView.as_view(), name='perfil-update'),
    path('<uuid:pk>/activar/', PerfilActivateView.as_view(), name='perfil-activate'),
    path('crear/', PerfilCreateView.as_view(), name='perfil-create'),
    path('<uuid:pk>/cargar-imagen/', ImagenCreateView.as_view(), name='imagen-create'),
    path('', PerfilListView.as_view(), name='perfil-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
