from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    contents = models.TextField()
    regist_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title