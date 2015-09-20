import aniso8601
from datetime import datetime

def datetime_from_ISO_string(ISO_string):
    """
    An utility function to convert ISO 8601 formatted datetime string to pythonic datetime object.
    Input: The ISO formatted string 
    Output: The pythonic datetime object, None is there is some error in conversion.
    """
    try:
        return aniso8601.parse_datetime(ISO_string)
    except:
        return None
