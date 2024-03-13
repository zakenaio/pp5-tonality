from django.db import models

# Create your models here.

class Contact(models.Model):
    """ Contact model asking for Name/Email/Message. """
    name = models.CharField(max_length=75, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name