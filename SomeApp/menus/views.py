from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def menu_view(request: WSGIRequest, url: str = ''):
    return render(request, 'menu.html', {'menu': url})
