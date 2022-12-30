from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_view(request: WSGIRequest):
    return render(request, 'index.html')


def electronica_view(request: WSGIRequest):
    return render(
        request,
        'electronica.html',
        context={
            'page_name': 'Электроника',
            'catalog': 'Электроника'
        }
    )
