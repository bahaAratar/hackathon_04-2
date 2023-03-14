from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)  # '1' -> sdjfhue8rb3457fgidysuif
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    freelancer = models.BooleanField(default=False)
    client = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    EXPERIENCE_CHOICES = (
        ('Less than a year', 'Less than a year'),
        ('More than a year', 'More than a year'),
        ('More than 3 years', 'More than 3 years'),
        ('More than 6 years', 'More than 6 years')
    )

    first_name = models.CharField(max_length=50) # all
    last_name = models.CharField(max_length=50) # all
    experience = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES, null=True, blank=True) # freelancer
    education = models.TextField(null=True, blank=True) # freelancer
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True) # all
    email = models.EmailField(unique=True) # all
    password = models.CharField(max_length=100) # all
    # username = None
    activation_code = models.CharField(max_length=50, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.first_name}'
    
    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code
