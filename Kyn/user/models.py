from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    website = models.URLField(blank=True)
    interests = models.ManyToManyField('user.Interest')
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_subscribed = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    role = models.ForeignKey('user.Role', on_delete=models.CASCADE)
    language = models.CharField(max_length=50, blank=True)

    # Add any additional fields or customizations to the User model
    # Example:
    # bio = models.TextField(blank=True)

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'user'


class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'user'


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'user'
