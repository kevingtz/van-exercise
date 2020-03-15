from django.contrib.gis.geos import Point

LAT_LNG_SRID = 4326


def create_point(longitude, latitude):
    return Point(longitude, latitude, srid=LAT_LNG_SRID)