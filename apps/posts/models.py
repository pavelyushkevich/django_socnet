from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    post = models.TextField('Post')
    date = models.DateTimeField('Date', auto_now_add=True)
    likes = models.IntegerField('Likes', default=0)
    views_count = models.IntegerField('Views', default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.date >= (timezone.now() - timedelta(days=7))

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField('Comment')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
