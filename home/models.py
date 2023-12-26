from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} - {self.email}'
    
class General:
    id: int
    name: str
    desc: str
    section: str
    img: str