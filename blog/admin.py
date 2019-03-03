from django.contrib import admin
from .models import Membre, Article, NewsLetter, Pays

class ArticleAdmin(admin.ModelAdmin):
    # Configuration de la liste d'articles
    list_display   = ('id','titre',  'auteur', 'created_at')
    list_filter    = ('auteur', )
    date_hierarchy = 'created_at'
    ordering       = ('created_at', )
    search_fields  = ('titre', 'contenu')
    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
            'fields': ('titre', 'auteur')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('contenu', )
        }),
    )

    # Colonnes personnalisées
    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut rajouter des points de suspension.
        """
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s…' % text
        else:
            return text
    apercu_contenu.short_description = 'Aperçu du contenu'


admin.site.register(Membre)
admin.site.register(Article, ArticleAdmin)
admin.site.register(NewsLetter)
admin.site.register(Pays)