from django.urls import path

from .views import menu_view

app_name = 'menus'

urlpatterns = [
    path('', view=menu_view, name='main_menu'),
    path('<path:url>', view=menu_view, name='submenu'),
]
