
from django import urls
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.acc , name="acceuil"),
    path('admin/', admin.site.urls),
    path('magasin/',include('magasin.urls')),
    path('blog/',include('blog.urls')),

]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
