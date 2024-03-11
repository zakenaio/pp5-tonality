from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Records(models.Model):
        
    class Meta:
        verbose_name = 'Records'

    category = models.ManyToManyField('Category', blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    releasedate = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_new_release = models.BooleanField(default=False, verbose_name="Is New Release")
    is_deal = models.BooleanField(default=False, verbose_name="Is Deal")
    is_clearance = models.BooleanField(default=False, verbose_name="Is Clearance")

    def __str__(self):
        return self.name