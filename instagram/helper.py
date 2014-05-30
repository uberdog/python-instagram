import calendar
from datetime import datetime
from django.utils.timezone import utc

def timestamp_to_datetime(ts):
    return datetime.utcfromtimestamp(float(ts)).replace(tzinfo=utc)


def datetime_to_timestamp(dt):
    return calendar.timegm(dt.timetuple())
