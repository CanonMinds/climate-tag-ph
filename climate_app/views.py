import json

from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic import ListView

from climate_app.models import DACMemberCountry
from climate_app.models import InitialModel


class SourceMapView(ListView):
    model = InitialModel
    template_name = "climate_app/dash_index.html"

    def get_context_data(self, **kwargs):
        source_map_plans_list = InitialModel.objects.all().distinct("sovereignty")

        """ FeatureCollection - Coordinate Serialization """
        # coordinate_query = serialize(
        #     'geojson', source_map_plans_list,
        #     geometry_field = 'coordinates',
        #     fields=('sovereignty',))

        # serialized_coordinates = json.loads(coordinate_query)

        coordinate_queries = InitialModel.objects.values(
            "id", "sovereignty", "geometry"
        ).distinct("sovereignty")

        geojson_format = {
            "type": "FeatureCollection",
            "name": "DATA",
            "crs": {
                "type": "name",
                "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"},
            },
        }

        features_list = []
        if coordinate_queries:
            for record in coordinate_queries:

                feature_format = {
                    "type": "Feature",
                    "properties": "",
                    "geometry": "",
                }

                coordinates = []
                coordinates.append((record["geometry"]))

                property_serializer = {}
                property_serializer["Sovereignty"] = record["sovereignty"]
                property_serializer["Attribute"] = ""

                geometry_serializer = {}
                geometry_serializer["type"] = "MultiPolygon"

                jsonDec = json.decoder.JSONDecoder()
                myPythonList = jsonDec.decode(record["geometry"])

                geometry_serializer["coordinates"] = myPythonList
                geometry_serializer["id"] = record["id"]

                feature_format["properties"] = property_serializer
                feature_format["geometry"] = geometry_serializer

                features_list.append(feature_format)

        geojson_format["features"] = features_list
        coordinate_query = json.dumps(geojson_format)

        context = super(ListView, self).get_context_data(**kwargs)
        context = {
            "coordinate_query": coordinate_query,
        }
        return context


def index(request):
    template_name = "climate_app/dash_base.html"
    return render(
        request,
        template_name,
    )


def dashboard(request):
    html = "<html><body>Climate App Contents.</body></html>"
    return HttpResponse(html)
