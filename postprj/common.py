from django.db import models 

class CommonAbstract(models.Model):
    created_at = models.DateTimeField(null=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
