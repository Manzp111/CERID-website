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



class FinancialReport(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    file = models.FileField(upload_to='reports/')

class ImpactMetric(models.Model):
    year = models.IntegerField()
    projects = models.IntegerField()
    people = models.IntegerField()
    regions = models.IntegerField()

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team/')

class LegalDocument(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')






