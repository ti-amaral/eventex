import uuid

from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=100,verbose_name="nome")
    cpf = models.CharField(max_length=11,verbose_name="CPF")
    email = models.EmailField(verbose_name="e-mail")
    phone = models.CharField(max_length=20,verbose_name="telefone")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="criado em")
    hashId = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    paid = models.BooleanField(default=False, verbose_name="pago")

    class Meta:
        verbose_name_plural = "inscrições"
        verbose_name = "inscrição"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name