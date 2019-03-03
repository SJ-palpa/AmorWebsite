from django.db import models
from django.utils import timezone


class Membre(models.Model):
    id = models.AutoField(primary_key=True, db_column='mem_id')
    nom = models.CharField(max_length=100, db_column='mem_nom')
    prenom = models.CharField(max_length=100, db_column='mem_auteur')
    mail = models.CharField(max_length=100, null=True, db_column='mem_mail')
    description = models.TextField(null=True, db_column='mem_description')
    titre = models.CharField(max_length=100, blank=True, null=True, db_column='mem_titre')
    created_at = models.DateTimeField(default=timezone.now, db_column='rmem_create_at')
    image = models.ImageField(blank=True, upload_to="img")

    class Meta:
        verbose_name = "Membre"
        verbose_name_plural = "Membre"
        ordering = ['nom']

    def __str__(self):
        return "{0} {1}".format(self.nom, self.prenom)


class Article(models.Model):
    id = models.AutoField(primary_key=True, db_column='art_id')
    titre = models.CharField(max_length=100, db_column='art_titre')
    auteur = models.ForeignKey(Membre, null=True, on_delete=models.CASCADE, db_column='art_auteur')    #lien membre
    contenu = models.TextField(null=True, db_column='art_contenu')
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Date de parution", db_column='art_date')

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"
        ordering = ['created_at']

    def __str__(self):
        return self.titre


class NewsLetter(models.Model):
    id = models.AutoField(primary_key=True, db_column='nle_id')
    titre = models.CharField(max_length=100, db_column='nle_titre')
    auteur = models.ForeignKey(Membre, null=True, on_delete=models.CASCADE, db_column='nle_auteur')    #lien membre
    contenu = models.TextField(null=True, db_column='nle_contenu')
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Date de parution", db_column='nle_date')

    class Meta:
        verbose_name = "NewsLetter"
        verbose_name_plural = "NewsLetters"
        ordering = ['created_at']

    def __str__(self):
        return self.titre


class Adherent(models.Model):
    id = models.AutoField(primary_key=True, db_column='adh_id')
    nom = models.CharField(max_length=100, db_column='adh_nom')
    prenom = models.CharField(max_length=100, db_column='adh_auteur')
    mail = models.TextField(null=True, db_column='adh_contenu')
    created_at = models.DateTimeField(default=timezone.now, db_column='adh_create_at')
    image = models.ImageField(blank=True, upload_to='adh_image')

    class Meta:
        verbose_name = "Adherent"
        verbose_name_plural = "Adherent"
        ordering = ['nom']

    def __str__(self):
        return "{0} {1}".format(self.nom, self.prenom)


class Pays(models.Model):
    id = models.AutoField(primary_key=True, db_column='pay_id')
    nom = models.CharField(max_length=100, db_column='pay_nom')
    representant = models.ManyToManyField(Membre, db_column='pay_representant')
    created_at = models.DateTimeField(default=timezone.now, db_column='pay_create_at')
    updated_at = models.DateTimeField(default=timezone.now, db_column='pay_date_update')

    class Meta:
        verbose_name = "Pays"
        verbose_name_plural = "Pays"
        ordering = ['nom']

    def __str__(self):
        return self.nom

