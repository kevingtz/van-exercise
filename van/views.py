from django.contrib.gis.db.models.functions import Distance
import json
from django.http import JsonResponse
from django.contrib.gis.measure import D
from django.views import View
from van.models import VanModel

from van.utils import create_point


class Van(View):
    name = 'API'

    @classmethod
    def _van_as_json(cls, van):
        van_json = {
            'id': van.id,
            'code': van.code,
            'lat': van.latitude,
            'lng': van.longitude
        }

        if hasattr(van, 'distance'):
            van_json['distance'] = van.distance.m

        return van_json

    def get(self, request, *args, **kwargs):
        """Return the nearest 200 vans sorted by distance.

        Only consider vans that are 500 meters or closer.
        """
        MAX_DISTANCE_METERS = 500
        MAX_VANS_TO_RETURN = 200

        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lng'))

        if not lat or not lng:
            raise Exception('Missing parameter')

        location = create_point(lng, lat)

        van_query = (
            VanModel
                .objects
                .filter(
                    location__distance_lte=(location, D(m=MAX_DISTANCE_METERS))
                )
                .annotate(distance=Distance('location', location))
                .order_by('distance')
        )[:MAX_VANS_TO_RETURN]

        vans_as_json = [self._van_as_json(van) for van in van_query]

        return JsonResponse({
            'vans': vans_as_json
        })

    def post(self, request, *args, **kwargs):
        """Create/Update a van."""
        data = json.loads(request.body)

        lat = float(data.get('lat'))
        lng = float(data.get('lng'))
        code = data.get('code')

        if not lat or not lng or not code:
            raise Exception('Missing parameter')

        location = create_point(lng, lat)

        try:
            van = VanModel.objects.get(code=code)
            van.location = location
            van.save()
        except VanModel.DoesNotExist:
            van = VanModel.objects.create(
                location=location,
                code=code
            )

        return JsonResponse(self._van_as_json(van))
