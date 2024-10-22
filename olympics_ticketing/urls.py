from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservations/', include('reservations.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Redirige la racine vers /reservations/
    path('', lambda request: HttpResponseRedirect('/reservations/')),
]
