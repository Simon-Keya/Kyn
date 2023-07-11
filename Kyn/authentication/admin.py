from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User  # Import the User model from the user directory models.py file

admin.site.register(User, UserAdmin)
