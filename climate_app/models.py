from django.db import models

# Create your models here.
class InitialModel(models.Model):
    sovereignty = models.CharField(max_length=100, null=False)
    geometry = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'