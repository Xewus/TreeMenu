from django.urls import path

from .views import index_view

app_name = 'example_app'

urlpatterns = [
    path('', view=index_view, name='index')
]
