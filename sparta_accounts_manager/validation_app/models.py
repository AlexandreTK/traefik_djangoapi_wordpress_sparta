from django.db import models

# Create your models here.

class UserLicense(models.Model):
    USER_STATUS = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    ACCOUNT_TYPE = (
        ('D', 'Demo'),
        ('R', 'Real'),
    )

    account_number = models.CharField(max_length=100, unique=True)
    account_broker = models.CharField(max_length=100)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE)

    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_status = models.CharField(max_length=1, choices=USER_STATUS)
    expiration_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Meta:
#   unique_together = ('user_email', 'account_number')
