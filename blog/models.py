from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    brithday = models.DateField(blank=True)
    email = models.EmailField(blank=True,null=True)
    def __unicode__(self):
        return smart_unicode(self.name)
    
class Passage(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(Author,null=True, blank=True)
    time = models.DateField(timezone.now)
    def __unicode__(self):
        return smart_unicode(self.title)
        
class Reply(models.Model):
    name = models.CharField(max_length=50,blank=True)
    body = models.TextField()
    time = models.DateField(timezone.now)
    inpassage = models.ForeignKey(Passage)
    def __unicode__(self):
        
        return smart_unicode(self.time)