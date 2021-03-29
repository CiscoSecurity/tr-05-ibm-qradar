from datetime import timedelta

from version import VERSION


class Config:
    VERSION = VERSION

    ARIAL_VERSION = '12.0'

    TOTAL_TIME_INTERVAL = timedelta(days=7)

    HEADERS = {
        'Accept': 'application/json',
        'Version': '12.0',
    }
    BASE_URI = '/api/'

    REFER_URL = (
        "https://{server_ip}/console/do/ariel/arielSearch?appName="
        "EventViewer&pageId=EventList&dispatch=performSearch"
        "&value(timeRangeType)=aqlTime&value(searchMode)=AQL&value(aql)="
        "SELECT * FROM events WHERE sourceip='{observable}' OR "
        "destinationip='{observable}' LAST 7 DAYS"
    )

    CTIM_DEFAULTS = {
        'schema_version': '1.1.4',
    }

    SOURCE = 'QRadar SIEM'

    SIGHTING_DEFAULTS = {
        **CTIM_DEFAULTS,
        'confidence': 'High',
        'count': 1,
        'type': 'sighting',
        'source': SOURCE,
    }

    RELATIONS_DEFAULTS = {
        "origin": 'QRadar SIEM',
        "relation": 'Connected_To'
    }

    QRADAR_OBSERVABLE_TYPES = [
        'ip'
    ]

    CTR_DEFAULT_ENTITIES_LIMIT = 100

    SEARCH_TIMOUT_IN_SEC = 40
