# -*- coding: utf-8 -*-
from django.views.generic import ListView, TemplateView
from figurinhas.models import Figurinha


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Figurinha.objects.all().count()
        return context

class AlbumView(ListView):
    template_name = 'album.html'
    context_object_name = 'figurinhas'

    def get_queryset(self):
        return Figurinha.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Figurinha.objects.all().count()
        context['tenho'] = Figurinha.objects.filter(tenho=True).count()
        context['faltam'] = context['total'] - Figurinha.objects.filter(tenho=True).count()
        if context['total'] == 0:
            context['porcento'] = 0
        else:
            context['porcento'] = round(float(context['tenho'] * 100 / context['total']), 2)
        context['rp'] = self.get_queryset().filter(quantidade__gt=0)
        context['repetidas'] = 0
        for r in context['rp']:
            context['repetidas'] += r.quantidade

        if self.request.GET.get('q'):
            context['figs'] = self.request.GET.get('q').upper().split(' ')
            context['encontrados'] = self.get_queryset().filter(nome__in=context['figs'], tenho=True).count()

        return context

class FaltamView(ListView):
    template_name = 'faltam.html'
    context_object_name = 'figurinhas'

    def get_queryset(self):
        return Figurinha.objects.filter(tenho=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Figurinha.objects.all().count()
        context['faltam'] = context['total'] - Figurinha.objects.filter(tenho=True).count()

        if self.request.GET.get('q'):
            context['figs'] = self.request.GET.get('q').upper().split(' ')
            context['encontrados'] = self.get_queryset().filter(nome__in=context['figs']).count()
    
        return context


class RepetidasView(ListView):
    template_name = 'repetidas.html'
    context_object_name = 'figurinhas'

    def get_queryset(self):
        return Figurinha.objects.filter(quantidade__gt=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        figurinhas = self.get_queryset()
        repetidas = 0
        for r in figurinhas:
            repetidas += r.quantidade

        if self.request.GET.get('q'):
            figs = self.request.GET.get('q').upper().split(' ')
            context['encontrados'] = figurinhas.filter(nome__in=figs).count()
        context['repetidas'] = repetidas
        return context


class InstallView(TemplateView):

    template_name = 'install.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            for i in list(range(681)):
                obj, created = Figurinha.objects.get_or_create(
                    nome=str(i),
                    usuario=self.request.user,
                    tenho=False
                )
            context['erro'] = False
        else:
            context['erro'] = True
        return context