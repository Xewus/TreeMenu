from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_view(request: WSGIRequest):
    return render(request, 'index.html')


def example_view(request: WSGIRequest):
    return render(
        request,
        'example.html',
        context={
            'greating': 'Hello!'
        }
    )
