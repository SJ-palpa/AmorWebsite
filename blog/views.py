from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Article,Membre,Pays

def home(request):
    return render(request, 'blog/accueil.html')

#------------------------------------------------------------------------------------------------

def notreHistoire(request):
    return render(request, 'blog/l_association/notreHistoire.html')

class ListeMembres(ListView):
    model = Membre
    context_object_name = "membres"
    template_name = "blog/l_association/nos_membres.html"
    queryset = Membre.objects.all() #prend tout les membres
    paginate_by = 5

def membre(request, mem_id):
    membreSelect = Membre.objects.get(id=mem_id)  # id du membre
    return render(request, 'blog/l_association/membre.html', {'article': membreSelect})

def nos_ambassadeurs(request):
    return render(request, 'blog/l_association/nos_ambassadeurs.html')


#------------------------------------------------------------------------------------------------

def hitech4orphans(request):
    return render(request, 'blog/nos_projets/hitech4orphans.html')

def gala_2019(request):
    return render(request, 'blog/nos_projets/gala_2019.html')

class ListeArticles(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/nos_projets/articles.html"
    queryset = Article.objects.all() #prend tout les articles
    paginate_by = 5


def article(request, art_id):
    articleSelect = Article.objects.get(id=art_id)  # id de l'article
    return render(request, 'blog/nos_projets/article.html', {'article': articleSelect})

#------------------------------------------------------------------------------------------------

def dev_bene(request):
    return render(request, 'blog/s_engager/dev_bene.html')

def dev_stagiaire(request):
    return render(request, 'blog/s_engager/dev_stagiaire.html')

def donner(request):
    return render(request, 'blog/s_engager/donner.html')


def contact(request):
    return render(request, 'blog/s_engager/contact.html')

#------------------------------------------------------------------------------------------------


def ecosoc_onu(request):
    return render(request, 'blog/amor_monde/ecosoc_onu.html')

def media(request):
    return render(request, 'blog/amor_monde/media.html')

class ListePays(ListView):
    model = Pays
    template_name = "blog/amor_monde/pays.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ListePays, self).get_context_data(**kwargs)
        paysSelect = Pays.objects.get(id=self.kwargs['pay_id'])
        paysTous = Pays.objects.all()
        context['group'] = {'paysSelect': paysSelect,'paysTous': paysTous}
        return context

def policy_papers(request):
    return render(request, 'blog/amor_monde/policy_papers.html')




def festiamor_2013(request):
    return render(request, 'blog/festiamor_2013.html')



