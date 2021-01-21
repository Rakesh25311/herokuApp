from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.core.urlresolvers import reverse  @dj1.8
from django.urls import reverse #dj2.x


# Create your models here.
class CustomManager(models.Model):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=264)
    slug = models.SlugField(max_length=264, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts',on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rakesh = models
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,
                                           self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
