from django.db import models

class Stores(models.Model):
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    info = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Store'

    def __str__(self):
        return self.name


class Customers(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    info = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True, default= 'defaults/default.png')

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Customer'

    def __str__(self):
        return self.name
