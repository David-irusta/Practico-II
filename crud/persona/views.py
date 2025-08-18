from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Persona
from django.contrib.auth.mixins import LoginRequiredMixin

class PersonaListview(LoginRequiredMixin, ListView):
    model = Persona
    template_name = 'persona/lista.html'
    context_object_name = 'persona'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Personas'
        return context
    
class PersonaDetailView(LoginRequiredMixin, DetailView):
    model = Persona
    template_name = 'persona/detalle.html'
    context_object_name = 'persona'

class PersonaCreateView(LoginRequiredMixin, CreateView):
    model = Persona
    template_name = 'persona/crear.html'
    fields = ['nombre', 'apellido', 'email', 'oficina']
    success_url = reverse_lazy('persona:lista')

class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    model = Persona
    template_name = 'persona/crear.html'
    fields = ['nombre', 'apellido', 'email', 'oficina']
    success_url = reverse_lazy('persona:lista')

class PersonaDeleteView(LoginRequiredMixin, DeleteView):
    model = Persona
    template_name = 'persona/eliminar.html'
    context_object_name = 'persona'
    success_url = reverse_lazy('persona:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context
    
class PersonaSearchView(LoginRequiredMixin, ListView):
    model = Persona
    template_name = 'persona/buscar.html'
    context_object_name = 'personas'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Persona.objects.filter(nombre__icontains=query)
        return Persona.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Buscar Personas'
        context['query'] = self.request.GET.get('q', '')
        return context

