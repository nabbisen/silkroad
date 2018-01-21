from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Ret

def index(request):
    template = loader.get_template('search/index.html')
    context = {
        'title': 'Search',
        'ret': Ret.objects.all(),
    }
    return HttpResponse(template.render(context, request))

