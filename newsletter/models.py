from django.db import models


class Newsletter(models.Model):
    """ Newsletter model asking for email address. """
    email = models.EmailField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.email
