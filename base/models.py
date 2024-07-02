from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

gender_choices = (('male', 'male'), ('female', 'female'))

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, default=0)
    avatar = models.ImageField(blank=True, null=True, upload_to='image/avatar')
    gender = models.CharField(blank=True, null=True, max_length=20, choices=gender_choices)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Ingredient(models.Model):
    name = models.CharField(max_length=40, default=str)
    description = models.CharField(max_length=100, blank=True, default=str)
    icon = models.ImageField(blank=True, null=True, upload_to='image/ingrediants')
    calorie = models.FloatField(default=1.0, verbose_name="Calorie in 100g")
    protein = models.FloatField(default=1.0, verbose_name="Protein in 100g")
    carbohydrates = models.FloatField(default=1.0, verbose_name="Carbohydrates in 100g")
    fat = models.FloatField(default=0.0, blank=True, verbose_name="Fat in 100g (optional)")
    sugar = models.FloatField(default=0.0, blank=True, verbose_name="Sugar in 100g (optional)")
    creatine = models.FloatField(default=0.0, blank=True, verbose_name="Creatine in 100g (optional)")
    glutamine = models.FloatField(default=0.0, blank=True, verbose_name="Glutamine in 100g (optional)")