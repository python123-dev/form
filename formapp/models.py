from django.db import models

# Create your models here.
class customer(models.Model):
    first_name=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.email

