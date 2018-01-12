from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('menu/index.html')
    context = {
        'title': 'Menu',
    }
    return HttpResponse(template.render(context, request))

