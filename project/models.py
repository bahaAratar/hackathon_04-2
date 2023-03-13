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
    title = models.SlugField(primary_key=True,unique=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='categories',blank=True,null=True)

    def __str__(self) -> str:
        return f'{self.title}'

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    is_active = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name}'