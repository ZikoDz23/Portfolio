from django.db import models

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    email = models.EmailField()
    photo = models.ImageField(upload_to='media/')
    def __str__(self) -> str:
        return self.full_name

class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/projects/')
    Project_desc = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title
    
class ProjectImages(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/projects/images/')

    def __str__(self):
        return f"Image for {self.project.title}"
    
    
class Skills(models.Model):
    skill = models.CharField(max_length=40)
    image = models.ImageField(upload_to='media/skills/')
    def __str__(self):
        return self.skill