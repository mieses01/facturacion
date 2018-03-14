from django.db import models

class compania(models.Model):
    rnc = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    num_fac = models.IntegerField()
    pref_ncf = models.CharField(max_length=30)
    sec_ncf = models.IntegerField()
    comprobante = models.CharField(max_length=2)
    num_max_comp = models.IntegerField()
