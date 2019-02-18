from django.shortcuts import render

from blog.form import ContactForm


def home(request):
    return render(request, 'blog/accueil.html')


def aPropos(request):
    return render(request, 'blog/aPropos.html')


def eCosoc(request):
    return render(request, 'blog/ecosoc.html')


def gouvernance(request):
    return render(request, 'blog/gouvernance.html')


def pays(request):
    return render(request, 'blog/pays.html')


def festiamor_2013(request):
    return render(request, 'blog/festiamor_2013.html')


def contribution(request):
    return render(request, 'blog/contribution.html')


