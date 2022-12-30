from django.urls import path

from .views import index_view, electronica_view

app_name = 'example_app'

urlpatterns = [
    path('', view=index_view, name='index'),
    path('electronica/', view=electronica_view, name='electronica')
]
