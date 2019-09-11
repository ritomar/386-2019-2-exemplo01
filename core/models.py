from django.db import models


class Tarefa(models.Model):
    descricao = models.CharField(max_length=100)
    feito = models.BooleanField()

    def __str__(self):
        return self.descricao
