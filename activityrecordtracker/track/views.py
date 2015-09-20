from rest_framework import status
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from track.backends  import log_an_activity,read_activities
from track.serializers import ActivitySerializer as Actser
import sys,inspect,logging, traceback
logger = logging.getLogger(__name__)

# We will be using class based views(ViewSets specifically) as there is good possibility for extending the functionality through various design patterns 

def api_marker_decorator(view_method):
    # mark the method as something that requires view's class
    view_method.is_api = True
    return view_method

class HelpViewSet(viewsets.ViewSet):
    
    renderer_classes = (JSONRenderer, )
    @list_route(methods=['get'])
    def list_apis(self,request):
        classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        apis=None
        for aclass in classes:
            if aclass[1].__module__ != __name__:
                continue
            methods=inspect.getmembers(aclass[1], predicate=inspect.ismethod)
            for method in methods:
                if 'bind_to_methods' in method[1].__dict__ :
                    description=method[1].__doc__
                    if apis is None:
                        apis=[]
                    apis.append({'API_name':method[1].__name__,'description':description})
        return Response({'Available API':apis}) 
        
        
class ActivityViewSet(viewsets.ViewSet):
    """
    List activity records matching the specified criteria.
    """
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer, )

    @api_marker_decorator
    @list_route(methods=['post'])    
    def log_activity(self,request):    
	"""
	Log an activity.
	"""
	querydict=request.data
        try:
	    results=log_an_activity(querydict)        
            data=results['data']
            result=results['success']
            if result:
	        return Response(data,status.HTTP_201_CREATED)	    
	    else:
	        return Response(data,status.HTTP_400_BAD_REQUEST)
	except:
	    logger.error(traceback.format_exc())
	    return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


        


    @api_marker_decorator
    @list_route(methods=['get'])    
    def activities(self,request):    
	"""
	Fetch activities filtered by specifying, username, feature_name, activity_datetime, parent_feature_name and activity_result
	"""
	querydict=request.GET
        username=querydict['username']
	from_datetime=querydict['from_datetime']
	to_datetime=querydict['to_datetime']
	parent_feature_name=querydict['parent_feature_name']
	feature_name=querydict['feature_name']
	activity_result=querydict['activity_result']
	try:
            activities = read_activities(username,from_datetime,to_datetime,parent_feature_name,feature_name,activity_result)
            activityserializer = Actser(activities, many=True)
	    data=activityserializer.data
	    return Response(data,status.HTTP_200_OK)
    	except:
	    logger.error(traceback.format_exc())
	    return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
	

