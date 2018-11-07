# -*- coding: UTF-8 -*-
import requests
from django.contrib import messages
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from app.models import Rsvp, Recado, Produto

from bs4 import BeautifulSoup

categoria = 'geladeira'

def get_americanas(categoria):
    base_url = 'https://www.americanas.com.br'
    url = base_url + '/busca/' + categoria
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.findAll("section", {"class": "card-product"})
    for item in items:
        url = base_url + item.find('a').get('href')
        img = item.find('a').find('img').get('src')
        nome = item.find('h1').text
        preco = item.find('div', {'class': 'card-product-price'}).findAll('span')[1].text
        parcelas = item.find('span', {'class': 'card-product-installments'}).text

        try:
            if not (Produto.objects.filter(nome=nome).exists() or Produto.objects.filter(url=url).exists()):
                produto = Produto(nome=nome, img=img, url=url, preco=preco, parcelas=parcelas, categoria=categoria)
                produto.save()
        except (Exception,):
            pass


def get_magazine_luiza(categoria):
    base_url = 'https://busca.magazineluiza.com.br/busca?q='
    url = base_url + categoria
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.findAll("li", {"class": "nm-product-item"})
    for item in items:
        url = 'https:' + item.find('a').get('href')
        img = 'https:' + item.find('img', {'class': 'nm-product-img'}).get('src')
        nome = item.find('h2', {'class': 'nm-product-name'}).text
        try:
            content = requests.get(url).content
            it = BeautifulSoup(content, 'html.parser')
            preco = it.find('span', {'class':'price-template__text'}).text
            parcelas = it.find('div', {'class': 'price-template'}).text
        except (Exception,):
            preco = ''
            parcelas = ''


        try:
            if not (Produto.objects.filter(nome=nome).exists() or Produto.objects.filter(url=url).exists()):
                produto = Produto(nome=nome, img=img, url=url, preco=preco, parcelas=parcelas, categoria=categoria)
                produto.save()
        except (Exception,):
            pass


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # get_magazine_luiza(categoria)
        context = self.get_context_data(**kwargs)
        context['recados'] = Recado.objects.filter(aprovado=True)
        return self.render_to_response(context)



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


def submit_recado(request):
    data = request.POST
    name = data.get('name')
    texto = data.get('message')
    # foto = data.get('photo')
    try:
        objeto = Recado(nome=name, texto=texto)
        objeto.save()
        # messages.success(request, u'Confirmação realizada com sucesso!')
        return JsonResponse({'message': u'Seu recado passará por aprovação dos noivos! Obrigado.'})
    except:
        # messages.error(request, u'Houve algum erro no formulário.')
        raise Http404
