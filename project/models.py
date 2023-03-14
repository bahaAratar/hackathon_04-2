from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# class Project():
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     category = ...
#     expirience = ...
#     subcategory = ...
#     description = models.TextField()
#     available = models.BooleanField(default=False)
#     price = models.DecimalField(max_digits=10,decimal_places=2)
#     comments = models.ForeignKey()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    experience = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.description[:50]


