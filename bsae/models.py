from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
standard_choices = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
)

SUBJECT_CHOICES = (
    ('Maths', 'Maths'),
    ('Science', 'Science'),
    ('English', 'English'),
    ('Social Science', 'Social Science'),
)

LANGUAGE_CHOICES = (
    ('English',"English"),
    ('Hindi',"Hindi"),
    ('Tamil','Tamil')
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    standard = models.CharField(max_length=10, choices=standard_choices)
    uuid = models.UUIDField(default=uuid.uuid4,unique=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    video = models.ManyToManyField('Video')
    image = models.ImageField(upload_to='covers')
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='English')
    standard = models.CharField(max_length=10, choices=standard_choices)
    material = models.FileField(upload_to='materials', blank=True, null=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title