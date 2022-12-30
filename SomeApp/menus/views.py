from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def catalog_view(request: WSGIRequest, url: str = ''):
    return render(request, 'menu.html', {'catalog': url})
