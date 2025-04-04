from django.contrib import admin
from .models import Todo  # Import the model you want to register

# Register the model with optional customization
admin.site.register(Todo)
