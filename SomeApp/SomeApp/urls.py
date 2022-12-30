from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('menu/', include('menus.urls', namespace='menus')),
    path('admin/', admin.site.urls),
    path('', include('example_app.urls', namespace='example_app'))
]
