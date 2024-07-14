from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField(upload_to='uploaded_photos/', null=False, blank=False)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.description
    

    