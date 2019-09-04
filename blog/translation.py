from modeltranslation.translator import translator, TranslationOptions
from blog.models import Article

class ArticleTranslationOptions(TranslationOptions):
    fields = ('titre', 'contenu',)

translator.register(Article, ArticleTranslationOptions)

