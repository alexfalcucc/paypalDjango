from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
#, verbose_name="Voce se considera programador? Marque:"
#para_voce = models.BooleanField(default=True, verbose_name="Voce se considera programador? Marque:")
class SignUp(models.Model):
    nome = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(verbose_name='Sobrenome',max_length=120, blank=True, null=True)
    email = models.EmailField()
    descricao = models.TextField()
    horario = models.DateTimeField(auto_now_add=True, auto_now=False)
    atualizado = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
            return smart_unicode(self.email)