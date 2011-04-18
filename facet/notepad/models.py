from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category)
    
    def __unicode__(self):
        return self.title





