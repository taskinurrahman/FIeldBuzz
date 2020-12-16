from django.db import models

# Create your models here.
class Password(models.Model):
  passkey=models.CharField(max_length=120)

  def __str__(self):
        return self.passkey