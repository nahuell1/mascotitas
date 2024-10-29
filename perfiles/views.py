from django.views.generic import DetailView, ListView, CreateView, UpdateView, FormView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from stronghold.views import StrongholdPublicMixin
from .models import Perfil, Imagen
from .forms import PerfilForm, ActivateForm
# Create your views here.

class PerfilDetailView(StrongholdPublicMixin, DetailView):
    model = Perfil
    def get(self, request, *args, **kwargs):
        if self.get_object().humano:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("perfiles:perfil-activate", pk=self.get_object().pk)


class PerfilActivateView(FormView):
    form_class = ActivateForm
    template_name = "perfiles/perfil_activate.html"
    def get_success_url(self):
        return reverse('perfiles:perfil-detail', kwargs={'pk': self.get_object().pk})
    
    def get_object(self):
        return get_object_or_404(Perfil, pk=self.kwargs.get("pk"))
    
    def form_valid(self, form):
        perfil = self.get_object()
        if form.cleaned_data.get("codigo_de_activacion") == perfil.codigo_de_activacion:
            perfil.humano = self.request.user
            perfil.save()
        else:
            messages.warning(self.request, "El código ingresado no es válido. Tenga en cuenta que se distinguen mayúsculas y minúsculas.")
        return super().form_valid(form)
    

class PerfilCreateView(CreateView):
    model = Perfil
    form_class = PerfilForm

    def get_success_url(self):
        return reverse('perfiles:perfil-detail', kwargs={'pk': self.object.pk})


class PerfilUpdateView(UserPassesTestMixin, UpdateView):
    model = Perfil
    fields = ['nombre', 'numero_de_telefono', 'fecha_de_nacimiento', 'ubicacion', 'biografia']

    def get_success_url(self):
        return reverse('perfiles:perfil-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.humano = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.get_object().humano:
            if self.get_object().humano == self.request.user:
                return True
            return False
        return True


class PerfilListView(StrongholdPublicMixin, ListView):
    model = Perfil
    context_object_name = 'perfiles'


class ImagenDetailView(StrongholdPublicMixin, DetailView):
    model = Imagen


class ImagenCreateView(CreateView):
    model = Imagen
    fields = ['imagen', 'descripcion', 'is_profile_picture']

    def get_success_url(self):
        return reverse('perfiles:perfil-detail', kwargs={'pk': self.object.perfil.pk})

    def form_valid(self, form):
        form.instance.perfil = get_object_or_404(Perfil, pk=self.kwargs['pk'])
        return super().form_valid(form)


class ImagenListView(ListView):
    model = Imagen
    context_object_name = 'imagenes'
