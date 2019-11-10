from django.db import models

from .utils import code_generator, create_shortcode
# Create your models here.

class KirrURLManager(models.Model):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.shortcode = code_generator()
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
    
    