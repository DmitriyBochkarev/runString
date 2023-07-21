from django.db import models
from datetime import datetime

class Requests(models.Model):
    text = models.CharField(max_length=2000)
    date = models.DateTimeField(default=datetime.utcnow)
    video = models.FileField(default='runString.mp4', upload_to='media')

    def __str__(self):
        return self.text