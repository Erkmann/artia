from django.contrib import admin
from django.urls import path, include

from app_home import urls as apphome
from app_projeto import urls as appprojeto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include(apphome)),
    path('', include(apphome)),
    path('projetos/', include(appprojeto)),
]
