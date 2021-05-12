import requests
from django.contrib.gis.geos import Polygon
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import Property
from .serializers import PropertySerializer


class PropertyViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def list(self, request):

        address = request.query_params.get("address")
        if not address:
            return Response(status=status.HTTP_404_NOT_FOUND)

        address_osm_id = (
            requests.get(
                f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
            )
            .json()[0]
            .get("osm_id")
        )
        bbox = requests.get(
            f"https://nominatim.openstreetmap.org/reverse?osm_id={address_osm_id}&format=json&polygon_geojson=1&osm_type=R"
        ).json()["geojson"]["coordinates"]

        if not bbox:
            return Response(status=status.HTTP_404_NOT_FOUND)

        poly = Polygon(tuple((x, y) for x, y in bbox[0]))
        query = Property.objects.filter(cordinates__intersects=poly)
        serializer = PropertySerializer(query, many=True)
        ctx = {
            "properties": serializer.data,
            "cordinates": bbox,
        }
        return Response(ctx, status=status.HTTP_200_OK)
