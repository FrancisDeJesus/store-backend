from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    price = models.FloatField(null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title