from modeltranslation.translator import translator, TranslationOptions
from blog.models import Article,Pays,Ambassadeur,Membre,NewsLetter

class ArticleTranslationOptions(TranslationOptions):
    fields = ('titre', 'contenu',)

class MembreTranslationOptions(TranslationOptions):
    fields = ('description', 'titre',)

class PaysTranslationOptions(TranslationOptions):
    fields = ('nom',)

class AmbassadeurTranslationOptions(TranslationOptions):
    fields = ('description',)

class NewsLetterTranslationOptions(TranslationOptions):
    fields = ('titre','contenu')


translator.register(Article, ArticleTranslationOptions)
translator.register(Membre, MembreTranslationOptions)
translator.register(Pays, PaysTranslationOptions)
translator.register(Ambassadeur, AmbassadeurTranslationOptions)
translator.register(NewsLetter, NewsLetterTranslationOptions)