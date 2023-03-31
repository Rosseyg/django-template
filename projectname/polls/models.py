import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)
    is_featured = models.BooleanField(default=False, null=True, blank=True)
    
    def published_last_week(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.choice_text