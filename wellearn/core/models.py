from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, blank=True, null=False)
    level = models.IntegerField(default=1)
    photo = models.ImageField(upload_to='user_photo', default='user_photo/user.png')
    address = models.CharField(max_length=255)
    points = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

COURSE_LEVEL = (
    ('BEGGINER', 'Beginner'),
    ('ADVANCE', 'Advance'),
    ('EXPERT', 'Expert')
)

class Course(models.Model):
    name = models.CharField(max_length=250)
    course_subtitle = models.CharField(max_length=100)
    rating = models.FloatField()
    lessons_number = models.IntegerField()
    level = models.CharField(choices=COURSE_LEVEL, max_length=8, default='BEGGINER')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name