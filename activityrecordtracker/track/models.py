from django.db import models


#The Following is a manager to ensure that common low level db access methods are injected in both the custom queryset classes. 
class FeatureManager(models.Manager):
	def get_query_set(self):
	    return self.model.FeatureQuerySet(self.model)
	    
	def __getattr__(self, attr, *args):
		return getattr(self.get_query_set(), attr, *args)

class ActivityManager(models.Manager):
	def get_query_set(self):
	    return self.model.ActivityQuerySet(self.model)
	    
	def __getattr__(self, attr, *args):
		return getattr(self.get_query_set(), attr, *args)



        

        
# Let us have a model mixin that can be reused(potentially) later on. It houses common attributes for a feature.
class Feature(models.Model):
    feature_name=models.CharField(max_length=20)
    parent_feature_name=models.CharField(max_length=20,blank=True)

    # Custom Queryset method for the Feature model.
    class FeatureQuerySet(models.QuerySet):
        def parent_features(self,parent_feature_name):
            return self.filter(parent_feature_name__exact=parent_feature_name)
        def named_features(self,feature_name):
            return self.filter(feature_name__exact=feature_name)

      
    class Meta:
        abstract = True


# A model that represents an activity and extends the feature model
class Activity(Feature):
    SUCCESS='S'
    FAILURE='F'
    ERROR='E'
    INPROGRESS='I'
    RESULT= ((SUCCESS, 'Success'),(FAILURE, 'Failure'),(ERROR,'Error'),(INPROGRESS,'In Progress'),)
    
    username=models.CharField(max_length=20,blank=True)
    activity_datetime = models.DateTimeField()
    activity_result=models.CharField(max_length=1,choices=RESULT,default=INPROGRESS,blank=True)     
    # Let us explicitly state the default manager.
    objects=models.Manager()    
    # And then instantiate the ActivityManager.
    activities=ActivityManager()
    # And the FeatureManager
    features=FeatureManager()

    
    class ActivityQuerySet(Feature.FeatureQuerySet):
        def activities_by_user(self,username):
            return self.filter(username__exact=username)
        def activities_in_time(self,from_datetime,to_datetime):
            return self.filter(activity_datetime__range=(from_datetime,to_datetime))
        def activities_by_result(self,activity_result):
            return self.filter(activity_result__exact=activity_result)

    def __str__(self):
        return 'Activity, '+str(self.activity_name)
    class Meta:
        get_latest_by = 'activity_datetime'        
#        ordering=['activity_name','activity_datetime']
        verbose_name = "Activity Record"
        

