from django.db import models

# Create your models here.
class Dashboard(models.Model):
    name = models.TextField()
    password = models.TextField()
    dob = models.TextField()
    mob = models.TextField()
    email = models.TextField()

    def __str__(self):
        return self.name