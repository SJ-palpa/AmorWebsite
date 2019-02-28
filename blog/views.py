from django.shortcuts import render

from blog.form import ContactForm


def home(request):
    return render(request, 'blog/accueil.html')

#------------------------------------------------------------------------------------------------

def notreHistoire(request):
    return render(request, 'blog/l_association/notreHistoire.html')

def nos_membres(request):
    return render(request, 'blog/l_association/nos_membres.html')

def nos_ambassadeurs(request):
    return render(request, 'blog/l_association/nos_ambassadeurs.html')


#------------------------------------------------------------------------------------------------

def hitech4orphans(request):
    return render(request, 'blog/nos_projets/hitech4orphans.html')

def gala_2019(request):
    return render(request, 'blog/nos_projets/gala_2019.html')

def articles(request):
    return render(request, 'blog/nos_projets/articles.html')

#------------------------------------------------------------------------------------------------

def dev_bene(request):
    return render(request, 'blog/s_engager/dev_bene.html')

def dev_stagiaire(request):
    return render(request, 'blog/s_engager/dev_stagiaire.html')

def donner(request):
    return render(request, 'blog/s_engager/donner.html')

#------------------------------------------------------------------------------------------------

def ecosoc_onu(request):
    return render(request, 'blog/amor_monde/ecosoc_onu.html')

def media(request):
    return render(request, 'blog/amor_monde/media.html')

def pays(request):
    return render(request, 'blog/amor_monde/pays.html')

def policy_papers(request):
    return render(request, 'blog/amor_monde/policy_papers.html')








def festiamor_2013(request):
    return render(request, 'blog/festiamor_2013.html')


def contribution(request):
    return render(request, 'blog/contribution.html')


