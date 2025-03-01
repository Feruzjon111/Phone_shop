from django.db import models


class Phone(models.Model):
    brand = models.CharField(max_length=70)
    model = models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_existence = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Phone'

    def __str__(self):
        return self.brand


class Comment(models.Model):
    phone = models.CharField(max_length=9)
    name = models.CharField(max_length=70)
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Comment'

    def __str__(self):
        return f"{self.name} - {self.text[:20]}"


