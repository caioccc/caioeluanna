# -*- coding: UTF-8 -*-

from django.contrib import messages
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from app.models import Rsvp


class IndexView(TemplateView):
    template_name = 'index.html'


def submit_rsvp(request):
    data = request.POST
    name = data.get('name')
    if 'cerimonia' in data:
        cerimonia = True
    else:
        cerimonia = False
    if 'recepcao' in data:
        recepcao = True
    else:
        recepcao = False
    message = data.get('message')
    email = data.get('email')
    try:
        objeto = Rsvp(nome=name, email=email, cerimonia=cerimonia, recepcao=recepcao, mensagem=message)
        objeto.save()
        # messages.success(request, u'Confirmação realizada com sucesso!')
        return JsonResponse({'message': u'Confirmação realizada com sucesso!'})
    except:
        # messages.error(request, u'Houve algum erro no formulário.')
        raise Http404