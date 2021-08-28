import json

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize
from django.views.generic import ListView

from climate_app.models import DACMemberCountry
from climate_app.models import InitialModel


class SourceMapView(ListView):
    model = InitialModel
    template_name = "climate_app/dash_source_map.html"

    def get_context_data(self, **kwargs):
        table_list = DACMemberCountry.objects.values(
            'year',
            'provider',
            'climate_dev_finance_commitment_current',
            'financial_instrument',
            'finance_type',
        )

        """Pagination Section"""
        page = self.request.GET.get('page', 1)
        paginator = Paginator(table_list, 20)
        try:
            table_data = paginator.page(page)
        except PageNotAnInteger:
            table_data = paginator.page(1)
        except EmptyPage:
            table_data = paginator.page(paginator.num_pages)

        process = True
        if process:
            """FeatureCollection - Coordinate Serialization"""
            coordinate_queries = (
                DACMemberCountry.objects.filter(
                    is_published=True,
                ).values(
                    "id",
                    "provider",
                    "country_code__geometry",
                    "provider",
                    "year",
                    "climate_dev_finance_commitment_current",
                    "financial_instrument",
                    "finance_type",
                )
            )

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

                    property_serializer = {}
                    property_serializer["Provider"] = record["provider"]
                    property_serializer["Year"] = record["year"]
                    if float(record["climate_dev_finance_commitment_current"]):
                        property_serializer[
                            "ClimateDevFinanceCommitmentCurrent"
                        ] = "$" + str(
                            float(record["climate_dev_finance_commitment_current"])
                        )
                    property_serializer["FinancialInstrument"] = record[
                        "financial_instrument"
                    ]
                    property_serializer["FinanceType"] = record["finance_type"]
                    property_serializer["Attribute"] = ""

                    geometry_serializer = {}
                    geometry_serializer["type"] = "MultiPolygon"

                    jsonDec = json.decoder.JSONDecoder()
                    myPythonList = jsonDec.decode(record["country_code__geometry"])

                    geometry_serializer["coordinates"] = myPythonList
                    geometry_serializer["id"] = record["id"]

                    feature_format["properties"] = property_serializer
                    feature_format["geometry"] = geometry_serializer

                    features_list.append(feature_format)

            geojson_format["features"] = features_list
            coordinate_query = json.dumps(geojson_format)
        else:
            coordinate_query = None

        context = super(ListView, self).get_context_data(**kwargs)
        context = {
            "coordinate_query": coordinate_query,
            "table_data": table_data,
        }
        return context


class ClimateObjectiveView(ListView):
    model = DACMemberCountry
    template_name = "climate_app/dash_climate_objective.html"

    def get_context_data(self, **kwargs):
        table_data = DACMemberCountry.objects.values(
            'year',
            'provider',
            'purpose_code',
            'sector',
            'sub_sector',
            'gender',
        )
        context = {
            "table_data": table_data,
        }
        return context


class SectoralFundingView(ListView):
    model = DACMemberCountry
    template_name = "climate_app/dash_sectoral_funding.html"

    def get_context_data(self, **kwargs):
        coordinate_queries = (
            DACMemberCountry.objects.filter(
                country_code__country_code__gt=101,
                country_code__country_code__lte=108,
            )
            .exclude(country_code__country_code__in=[105, 106])
            .values(
                "id",
                "provider",
                "country_code__geometry",
                "provider",
                "year",
                "climate_dev_finance_commitment_current",
                "financial_instrument",
                "finance_type",
            )
        )

        context = super(ListView, self).get_context_data(**kwargs)
        context = {
            "coordinate_query": coordinate_queries,
        }
        return context


def index(request):
    template_name = "climate_app/dash_index.html"
    return render(
        request,
        template_name,
    )


def dashboard(request):
    html = "<html><body>Page under Construction.</body></html>"
    return HttpResponse(html)
