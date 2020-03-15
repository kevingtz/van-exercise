from django.contrib.gis.db.models import PointField
from django.db import models

from van.utils import LAT_LNG_SRID, create_point


class VanModel(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=6)
    location = PointField(srid=LAT_LNG_SRID, spatial_index=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.code)

    class Meta:
        db_table = 'van'

    @property
    def latitude(self):
        return self.location.y

    @latitude.setter
    def latitude(self, value):
        self.location = create_point(self.longitude, value)

    @property
    def longitude(self):
        return self.location.x

    @longitude.setter
    def longitude(self, value):
        self.location = create_point(value, self.latitude)

