from django.db import models
from django.utils.text import slugify
import uuid


class Segment(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default=uuid.uuid1)


    def __str__(self):
        return self.name
        
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Segment, self).save(*args, **kwargs)


class UkCompany(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100, null=True, blank=True)
    funding_status = models.CharField(max_length=80, blank=True, null=True)
    estimated_number_of_employees = models.CharField(max_length=30, blank=True)
    total_funding = models.CharField(default='', null=True, blank=True, max_length=100)
    estimated_revenue = models.CharField(max_length=80, blank=True, null=True)
    last_funding_date = models.CharField(max_length=50, blank=True, null=True)
    last_funding_type = models.CharField(max_length=80, blank=True, null=True)


    def __str__(self):
        return self.name

