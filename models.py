from django.db import models

# Create your models here.


class If(models.Model):
    journal = models.CharField(max_length=200, blank=False)
    iff = models.FloatField()
    year = models.CharField(max_length=4, blank=False)

    def __str__(self):
        return '-'.join([self.journal, self.year])
