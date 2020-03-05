from django.template import loader
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from blog.form import ContactForm
from blog.models import Article, Membre, Pays, Ambassadeur
from django.shortcuts import render

def home(request):
    articles = Article.objects.all().order_by('-created_at')[:3]
    return render(request, 'blog/accueil.html',{'articles' : articles})

#------------------------------------------------------------------------------------------------

def notreHistoire(request):
    return render(request, 'blog/l_association/notreHistoire.html')

class ListeMembres(ListView):
    model = Membre
    context_object_name = "membres"
    template_name = "blog/l_association/nos_membres.html"
    queryset = Membre.objects.all() #prend tout les membres
    paginate_by = 6

def membre(request, mem_id):
    membreSelect = Membre.objects.get(id=mem_id)  # id du membre
    return render(request, 'blog/l_association/membre.html', {'membre': membreSelect})

class nos_ambassadeurs(ListView):
    model = Ambassadeur
    context_object_name = "Ambassadeurs"
    template_name = "blog/l_association/nos_ambassadeurs.html"
    queryset = Ambassadeur.objects.all() #prend tout les ambassadeurs
    paginate_by = 10


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
    return http.HttpResponseServerError()
    #return render(request, 'blog/nos_projets/article.html', {'article': articleSelect})

#------------------------------------------------------------------------------------------------

def dev_bene(request):
    return render(request, 'blog/s_engager/dev_bene.html')

def dev_stagiaire(request):
    return render(request, 'blog/s_engager/dev_stagiaire.html')

def donner(request):
    return render(request, 'blog/s_engager/donner.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['name']
            prenom = form.cleaned_data['firstname']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            html_message = loader.render_to_string(
                'blog/email/email_contact_form.html',
                {
                    'nom': nom,
                    'prenom': prenom,
                    'message': message,
                    'from_email': from_email,
            }
            )
            try:
                send_mail("A.M.OR site web", "", 'stephanejermini@amor-association.org', ['jerministephane@gmail.com'], fail_silently=False, html_message=html_message)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "blog/s_engager/contact.html", {'form': form,'success': True})
    else:
        form = ContactForm()
    return render(request, "blog/s_engager/contact.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')

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


#------------------------------------------------------------------------------------------------
#--------------------------            Pages d erreurs          ---------------------------------
#------------------------------------------------------------------------------------------------

def handler404(request, exception):
    data = {}
    return render(request, 'blog/errorPages/404.html', data)


def handler500(request):
    return render(request, 'blog/errorPages/500.html', {}, status=500)
