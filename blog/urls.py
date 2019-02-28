from django.urls import path
from django.contrib import admin

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil', views.home, name="accueil"),

    path('l_association/notreHistoire', views.notreHistoire, name="notreHistoire"),
    path('l_association/nos_membres', views.nos_membres, name="nos_membres"),
    path('l_association/nos_ambassadeurs', views.nos_ambassadeurs, name="nos_ambassadeurs"),

    path('nos_projet/hitech4orphans', views.hitech4orphans, name="hitech4orphans"),
    path('nos_projet/gala_2019', views.gala_2019, name="gala_2019"),
    path('nos_projet/articles', views.articles, name="articles"),

    path('s_engager/Devenir_Benevole', views.dev_bene, name="dev_bene"),
    path('s_engager/dev_stagiaire', views.dev_stagiaire, name="dev_stagiaire"),
    path('s_engager/donner', views.donner, name="donner"),

    path('amor_monde/ecosoc_onu', views.ecosoc_onu, name="ecosoc_onu"),
    path('amor_monde/media', views.media, name="media"),
    path('amor_monde/pays', views.pays, name="pays"),
    path('amor_monde/policy_papers', views.policy_papers, name="policy_papers"),


    path('festiamor_2013', views.festiamor_2013, name="festiamor_2013"),
    path('contribution', views.contribution, name="contribution"),
]