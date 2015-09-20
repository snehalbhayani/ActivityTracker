from django.db import models

from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Feature(TimeStampedModel):
    """
    Let the Django website comprise of various features. Each activity by a user will be a bunch of features,
    each used for specific amounts of time.
    """
    feature_created_by=models.ForeignKey(User,related_name='Feature_Creator')      
    feature_modified_by=models.ForeignKey(User,related_name='Feature_Modifier')
    name=models.CharField(db_index=True,max_length=20,unique=True)
    slug=models.TextField(blank=True)
    desc=models.TextField(blank=True)
    
    def __str__(self):
        return str(name)

        
