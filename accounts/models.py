from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=256)
    ZIP_code = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    avatar = models.ImageField()

    ROLES_CHOICES = (
        ("ADM", "Admin"),
        ("USR", "User")
    )
    role = models.CharField(
        max_length=3,
        choices=ROLES_CHOICES,
        default="USR",
    )

    COMM_CHOICES = (
        ("MAIL", "post mail"),
        ("EMAIL", "email")
    )
    preferred_communication_channel = models.CharField(
        max_length=5,
        choices=COMM_CHOICES,
        default="EMAIL",
    )

    def __str__(self):
        if self.user.first_name:
            return self.user.first_name
        return self.user.username



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name} {self.surname}'