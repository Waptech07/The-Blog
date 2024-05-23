from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from django.core.validators import FileExtensionValidator
from django.forms import CheckboxSelectMultiple
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Generate a unique slug for the category based on the name
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    img = models.ImageField(default="", upload_to='images_uploaded', null=False)
    video = models.FileField(default="", upload_to='videos_uploaded', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv', 'gif'])])
    time = models.TimeField(default=timezone.now())
    date = models.DateField(default=date.today())
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    subheading = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Generate a unique slug for the post based on the title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.post.title} at {self.created_at}"

class Project(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    img = models.ImageField(default="", upload_to='projects_uploaded', null=False)
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Generate a unique slug for the project based on the title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
