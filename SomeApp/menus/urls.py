from django.urls import path

from .views import catalog_view

app_name = 'menus'

urlpatterns = [
    path('', view=catalog_view, name='main_menu'),
    path('<path:url>', view=catalog_view, name='submenu'),
]
