from django.db import models

# Create your models here.


class If(models.Model):
    journal = models.CharField(max_length=100, blank=False)
    iff = models.CharField(max_length=10, blank=False)
    year = models.CharField(max_length=4, blank=False)

    def __str__(self):
        return '-'.join([self.journal, self.year])
