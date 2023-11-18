from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.forms import CheckboxSelectMultiple


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    categories = [
        ('Technology', 'Technology'),
        ('Business','Business') ,
        ('Web Development','Web Development'),
        ('Mobile Development','Mobile Development'),
        ('Politics' ,'Politics')
    ]
    category = models.CharField(max_length=20, choices=categories)
    img = models.ImageField(default="", upload_to='images_uploaded', null=False)
    video = models.FileField(default="", upload_to='videos_uploaded', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv', 'gif'])])
    time = models.TimeField(default=timezone.now())
    date = models.DateField(default=date.today())
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    subheading = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(post):
        return f"{post.title}"


class Project(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    img = models.ImageField(default="", upload_to='projects_uploaded', null=False)


    def __str__(project):
            return f"{project.title}"