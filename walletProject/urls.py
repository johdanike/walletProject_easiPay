from django.contrib import admin
from django.urls import path, include
from wallet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallet/', include('wallet.urls')),
    path('', views.welcome),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
