from django.db import models
from django.contrib.auth.models import Permission, User

from django.urls import reverse

# Create your models here.

class Kategorie(models.Model):
    kuerzel = models.CharField(("Kürzel"), max_length=15)
    beschreibung = models.TextField(("Beschreibung"), blank=True, null=True)

    class Meta:
        verbose_name = ("Kategorie")
        verbose_name_plural = ("Kategorien")

    def __str__(self):
        return f"{self.kuerzel} ({self.beschreibung})"

    def get_absolute_url(self):
        return reverse("Kategorie_detail", kwargs={"pk": self.pk})

class Stufe(models.Model):
    stufe = models.IntegerField(("Stufe"), primary_key=True)
    beschreibung = models.TextField(("Beschreibung"))

    class Meta:
        verbose_name = ("Stufe")
        verbose_name_plural = ("Stufen")

    def __str__(self):
        return f"{self.stufe} - {self.beschreibung}"

    def get_absolute_url(self):
        return reverse("Stufe_detail", kwargs={"pk": self.pk})

class Karteikarte(models.Model):
    frage = models.TextField(("Frage"))
    antwort = models.TextField(("Antwort"))
    kategorie = models.ForeignKey(Kategorie, verbose_name=("Kategorie"), on_delete=models.RESTRICT)
    stufe = models.ForeignKey(Stufe, verbose_name=("Stufe"), on_delete=models.RESTRICT, default=1)
    erstelldatum = models.DateField(("Erstellt am"), auto_now=False, auto_now_add=True)
    aenderungsdatum = models.DateField(("Geändert am"), auto_now=True, auto_now_add=False)
    ersteller = models.ForeignKey(User, verbose_name=("Ersteller"), on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = ("Karteikarte")
        verbose_name_plural = ("Karteikarten")

    def __str__(self):
        return self.frage

    def get_absolute_url(self):
        return reverse("Karteikarte_detail", kwargs={"pk": self.pk})

class UserKK(models.Model):
    karteikarte = models.ForeignKey(Karteikarte, verbose_name=("Karteikarte"), on_delete=models.CASCADE)
    benutzer = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    count = models.IntegerField(("Anzahl Versuche"))
    lerndatum = models.DateField(("Geübt am"), auto_now=True, auto_now_add=False)
    gewusst = models.BooleanField(("Antwort gewusst"), default=False)

    class Meta:
        verbose_name = ("User - Karteikarte")
        verbose_name_plural = ("User - Karteikarten")

    def __str__(self):
        return f"{self.karteikarte} - {self.benutzer} ({self.count} / {self.gewusst})"

    def get_absolute_url(self):
        return reverse("UserKK_detail", kwargs={"pk": self.pk})
