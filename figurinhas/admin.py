# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Figurinha


class FigurinhaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'brilhante', 'tenho', 'usuario', 'data')
    search_fields = ('nome', )
    list_filter = ['tenho', 'brilhante']
    list_editable = ['tenho', 'quantidade']
    read_only = ['usuario', 'data']
    exclude = ['usuario', ]


    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.usuario = user
        instance.save()
        return instance

admin.site.register(Figurinha, FigurinhaAdmin)