from django.db import models
from django.utils import timezone

class Sequence(models.Model):
    uuid                 = models.CharField(max_length=100, null=False)
    user_id              = models.IntegerField(null=False)
    title                = models.CharField(max_length=100, null=False)
    file                 = models.TextField(null=True)
    file_path            = models.FileField(null=True)
    note                 = models.TextField(null=True)
    nb_bases             = models.IntegerField(null=True)
    nb_a                 = models.IntegerField(null=True)
    nb_c                 = models.IntegerField(null=True)
    nb_g                 = models.IntegerField(null=True)
    nb_t                 = models.IntegerField(null=True)
    percentage_a         = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    percentage_c         = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    percentage_g         = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    percentage_t         = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    percentage_gc        = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    percentage_at        = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    date                 = models.DateField(default=timezone.now, verbose_name="Date de création")