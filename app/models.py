from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Rsvp(TimeStamped):
    class Meta:
        verbose_name = "RSVP"
        verbose_name_plural = "RSVP's"
    cerimonia = models.BooleanField()
    recepcao = models.BooleanField()
    nome = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    mensagem = models.TextField()

    def __unicode__(self):
        return u'%s - %s' % (self.nome, self.email)
