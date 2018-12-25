from django.db import models

# Create your models here.


class BlogPost(models.Model):
    """文章"""
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()  # 时间戳

    """严格来说有四个变量，Django会默认为model加上一个id"""

    class Meta:
        ordering = ['-timestamp']

