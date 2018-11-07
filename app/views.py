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
            preco = it.find('span', {'class': 'price-template__text'}).text
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
    template_name = 'index_2.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['itens'] = Produto.objects.all()
        return self.render_to_response(context)


def submit_rsvp(request):
    data = request.POST
    categoria = data.get('categoria')
    type = data.get('loja')
    print(categoria)
    print(type)
    if type == 'ml' and categoria:
        try:
            get_magazine_luiza(categoria)
            return JsonResponse({'message': u'Confirmação realizada com sucesso!'})
        except:
            raise Http404
    elif type == 'americanas' and categoria:
        try:
            get_americanas(categoria)
            return JsonResponse({'message': u'Confirmação realizada com sucesso!'})
        except:
            raise Http404
    else:
        raise  Http404
