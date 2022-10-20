from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # admin panel.
    path('admin/', admin.site.urls),
    # documentation.
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    # api.
    path('api/', include('api.urls')),
]
