# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Figurinha(models.Model):
    nome = models.CharField(u'Número', max_length=255, unique=True)
    tenho = models.BooleanField(default=True)
    brilhante = models.BooleanField(default=False)
    quantidade = models.IntegerField(u'Quantidade de figurinhas repetidas', default=0, null=True, blank=True)
    data = models.DateTimeField(u'Data de modificação', auto_now=True, editable=False, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=False)
    

    class Meta:
        ordering = ['id', ]
        verbose_name = u'Figurinha'
        verbose_name_plural = u'Figurinhas'
        
    def __unicode__(self):
        return "%s" % self.nome