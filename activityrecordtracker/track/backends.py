from track.models import Activity
from track.serializers import ActivitySerializer
from track import utils
import traceback

def log_an_activity(dictionary_of_parameters):
    """
    A wrapper function to log an activity.
    INPUT: username - the username of the user who performed the activity.
           activity_datetime - Date and time in ISO 8601 format as a string when the activity was performed.
           parent_feature_name - Name of the parent activity, as a part of which this activity was performed.
           feature_result - Result of the activity.
    OUTPUT: If the save is a success, True is returned. In case of an error, False is returned.    
    """

    try:
        results={}
	activityserializer = ActivitySerializer(data=dictionary_of_parameters)
        if activityserializer.is_valid():    
	    activityserializer.save()
	    results['success']=True
	    results['data']=activityserializer.data
        else:
	    results['success']=False
	    results['data']=activityserializer.errors
        return results
    except:
	raise 


            
            
def read_activities(username=None,from_datetime=None,to_datetime=None,parent_feature_name=None,feature_name=None,activity_result=None):
    """
    A wrapper function to read activities
    INPUT: username - the username of the user who performed the activity.
           from_datetime & to_datetime - Date and time range specified for looking the activities up.
           activity_name - The Name of the activity to be looked up.
           parent_activity_name - Name of the parent activity, as a part of which this activity was performed.
           activity_result - Result of the activity.
    OUTPUT: If the save is a success, True is returned. In case of an error, False is returned.    
    """
    #Converting the ISO formatterd datetime strings to pythonic datetimes
    from_datetime=utils.datetime_from_ISO_string(from_datetime)
    to_datetime=utils.datetime_from_ISO_string(to_datetime)

    features=Activity.features
    activities=Activity.activities
    
    results=activities.activities_by_user(username)
    results=results.activities_in_time(from_datetime,to_datetime)
    results=results.parent_features(parent_feature_name)
    results=results.named_features(feature_name)
    results=results.activities_by_result(activity_result)    
	
    return list(results)


    
    
    
    
