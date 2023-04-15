from django.db import models
from django.contrib.auth.models import User

class Hackathonm(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathons')
    hackathon_image = models.ImageField(upload_to='hackathons')
    SUBMISSION_TYPES = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]
    submission_type = models.CharField(max_length=10, choices=SUBMISSION_TYPES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.CharField(max_length=255)

class Submission(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField()
    submission_file = models.FileField(upload_to='submissions')
    hackathon = models.ForeignKey(Hackathonm, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathonm, on_delete=models.CASCADE)


