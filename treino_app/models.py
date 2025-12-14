from django.db import models
from django.contrib.auth.models import User


class Exercicio(models.Model):
    nome = models.CharField(max_length=200)
    gif_url = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class FichaTreino(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome} - {self.usuario.username}"


class ItemFicha(models.Model):
    ficha = models.ForeignKey(FichaTreino, related_name="itens", on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    series = models.PositiveIntegerField()
    repeticoes = models.PositiveIntegerField()
    peso = models.FloatField()

    def __str__(self):
        return f"{self.exercicio.nome} - {self.series}x{self.repeticoes} @ {self.peso}kg"


from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    nome_completo = models.CharField(max_length=150, null=True, blank=True)
    idade = models.PositiveIntegerField(null=True, blank=True)
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    altura_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
