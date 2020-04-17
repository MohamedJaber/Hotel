from django.db import models


class guest(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class booking(models.Model):
    name = models.CharField(default='null', max_length=20)
    check = models.DateField()
    checkout = models.DateField()
    type = models.CharField(default='single', max_length=10)
    guest = models.OneToOneField(guest, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
