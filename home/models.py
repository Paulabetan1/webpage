from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} - {self.email}'
