from django.db import models

class UserRegistrationModel(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('activated', 'Activated'),
    )

    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'UserRegistrations'
