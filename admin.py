from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from travel.models import *
from import_export import resources

# Register your models here.

class TravelAutorizationResource(resources.ModelResource):
    class Meta:
        model = TravelAutorization
class TravelAutorizationAdmin(ImportExportModelAdmin):
    resource_class = TravelAutorizationResource
admin.site.register(TravelAutorization, TravelAutorizationAdmin)

class DetailMissionResource(resources.ModelResource):
    class Meta:
        model = DetailMission
class DetailMissionAdmin(ImportExportModelAdmin):
    resource_class = DetailMissionResource
admin.site.register(DetailMission, DetailMissionAdmin)

class CarRequestResource(resources.ModelResource):
    class Meta:
        model = CarRequest
class CarRequestAdmin(ImportExportModelAdmin):
    resource_class = CarRequestResource
admin.site.register(CarRequest, CarRequestAdmin)

class PersonTravelingResource(resources.ModelResource):
    class Meta:
        model = PersonTraveling
class PersonTravelingAdmin(ImportExportModelAdmin):
    resource_class = PersonTravelingResource
admin.site.register(PersonTraveling, PersonTravelingAdmin)

class RouteTravelResource(resources.ModelResource):
    class Meta:
        model = RouteTravel
class RouteTravelAdmin(ImportExportModelAdmin):
    resource_class = RouteTravelResource
admin.site.register(RouteTravel, RouteTravelAdmin)

class AproveTravelAutorizationResource(resources.ModelResource):
    class Meta:
        model = AproveTravelAutorization
class AproveTravelAutorizationAdmin(ImportExportModelAdmin):
    resource_class = AproveTravelAutorizationResource
admin.site.register(AproveTravelAutorization, AproveTravelAutorizationAdmin)
