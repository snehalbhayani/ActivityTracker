from django.contrib.auth import authenticate
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from views import ActivityViewSet, HelpViewSet


router = routers.SimpleRouter()
# Here we register all views for looking up various details about words using wordnet apis. 
#router.register(r'v1/wordnet/(?P<arg1>.+)/(?P<arg2>.+)/(?P<arg3>(.*))', LookupWordViewSet,base_name='wordnet')
router.register(r'v1/activitytracker', ActivityViewSet,base_name='activitytracker')
router.register(r'v1/activitytracker/help', HelpViewSet,base_name='activitytracker_APIdetails')
urlpatterns = router.urls
