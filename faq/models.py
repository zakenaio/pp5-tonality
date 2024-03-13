from django.db import models

# Create your models here.
class FAQ(models.Model):
    """ FAQs model with a question and answer. """
    question = models.CharField(max_length=250, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name_plural = "FAQs"
        ordering = ["question"]

    def __str__(self):
        return self.question
    

class Newsletter(models.Model):
    """ Newsletter model asking for email address. """
    email = models.EmailField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.email
