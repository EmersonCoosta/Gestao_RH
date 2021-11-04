from django.db import models


class RegistroHoraExtra(models.Model):
    registro = models.CharField(max_length=100)

    def __str__(self):
        return self.regitro
