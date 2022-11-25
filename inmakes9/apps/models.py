from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=250)
    disc=models.TextField()
    img=models.ImageField(upload_to='pics')
    year=models.IntegerField()

    def __str__(self):
        return self.name

