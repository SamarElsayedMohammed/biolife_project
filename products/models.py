import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Caregory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name





class Product(models.Model):
    id = models.UUIDField( # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
                Caregory,
                on_delete=models.CASCADE,
                )
    tags = models.ManyToManyField(Tag)
    
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta: # new
            permissions = [
            ('special_status', 'Can read all products'),
            ]

    def __str__(self):
        return self.name

    def get_absolute_url(self): # new
        return reverse('product_details', args=[str(self.id)])

    


class Review(models.Model): # new
    product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.review