from django.db import models
from django.contrib.auth.hashers import make_password

class Account(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.pk is None:  # Only hash the password if the account is new
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Account: {self.email}"