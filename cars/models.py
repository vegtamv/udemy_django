from django.db import models

# Create your models here.
class Car(models.Model):
    # pk
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return f"Car is {self.brand} {self.year}"
    

class CarReview(models.Model):
    #pk
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    review = models.CharField(max_length=100) 
    stars = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.last_name} {self.first_name}({self.email}): {self.stars} \n{self.review}"