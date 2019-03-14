from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Logo(models.Model):
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
def __str__(self):
        return self.title