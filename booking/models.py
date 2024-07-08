from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='booking_user_set',  # Change related_name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='booking_user_set',  # Change related_name to avoid conflict
        blank=True
    )

class VaccinationCenter(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    working_hours = models.CharField(max_length=100)

class VaccinationSlot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    center = models.ForeignKey(VaccinationCenter, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=100)
    class Meta:
        unique_together = ('center', 'date', 'time_slot')
