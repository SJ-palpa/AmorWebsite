from django.urls import path
from django.contrib import admin

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil', views.home, name="accueil"),
    path('aPropos', views.aPropos, name="aPropos"),
    path('ecosoc', views.eCosoc, name="ecosoc"),
    path('gouvernance', views.gouvernance, name="gouvernance"),
    path('pays', views.pays, name="pays"),
    path('festiamor_2013', views.festiamor_2013, name="festiamor_2013"),
    path('contribution', views.contribution, name="contribution"),
]