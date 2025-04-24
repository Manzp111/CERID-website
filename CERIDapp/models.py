from django.db import models


class LeaderTeam(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/leader_team/')

    def __str__(self):
        return self.name


class Partners(models.Model):
    name=models.CharField(max_length=100)
    county=models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/partner/')

    def __str__(self):
        return f"{self.name}-{self.county}-{self.image}"


class ImageSlider(models.Model):
    image = models.ImageField(upload_to='images/imgSlider/')
    caption=models.CharField(max_length=100)










