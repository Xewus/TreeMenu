from django.urls import path

from .views import index_view, computers_view

app_name = 'example_app'

urlpatterns = [
    path('', view=index_view, name='index'),
    path('computers/', view=computers_view, name='computers')
]
