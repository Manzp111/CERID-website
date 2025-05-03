from django.db import models
from django.utils.text import slugify



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


class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    button_text = models.CharField(max_length=50)
    button_link = models.CharField(max_length=200, blank=True)
    background_image = models.ImageField(upload_to='hero_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class VisionItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='vision_icons/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Project(models.Model):
    PROJECT_STATUS = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    status = models.CharField(max_length=20, choices=PROJECT_STATUS)
    completion_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    details_page_content = models.TextField(blank=True)
    testimonial = models.TextField(blank=True)
    report_file = models.FileField(upload_to='project_reports/', null=True, blank=True)
    
    # For completed projects
    key_achievements = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"





