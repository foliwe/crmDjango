from django.db import models

# Create your models here.


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=125)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
