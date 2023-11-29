from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from contract.models import Contract
from custom.models import Car, Munisipiu
from django.core.validators import FileExtensionValidator

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class TravelAutorization(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=False, blank=False, related_name="TravelAutorizationcontract")
    departure_date = models.DateField()
    place_of_departure = models.CharField(max_length=100, null = False, blank = False)
    return_date = models.DateField()
    purpose_of_travel = models.CharField(max_length=100, null = False, blank = False)
    project_name = models.CharField(max_length=100, null = False, blank = False)
    is_draft = models.BooleanField(default=True)
    is_aproved = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="TravelAutorizationcreatedby")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="TravelAutorizationupdatedby")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="TravelAutorizationdeletedby")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.purpose_of_travel}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='1-Data-Purchase_Request-Travel_Autorization'


class DetailMission(models.Model):
    # mission = models.ForeignKey(Mission, on_delete=models.CASCADE, null=True, blank=False, related_name="DetailMissionmission")
    travel_autorization = models.ForeignKey(TravelAutorization, on_delete=models.CASCADE, null=True, blank=False, related_name="DetailMissiontravelautorization")
    file = models.FileField(upload_to="upload_mission", null=True, blank=True,
			validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Attach Mission File")

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="DetailMissioncreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="DetailMissionupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="DetailMissiondeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.travel_autorization}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='10-Data-Custom-DetailMission'


class CarRequest(models.Model):
    travel_autorization = models.ForeignKey(TravelAutorization, on_delete=models.CASCADE, null=True, blank=False, related_name="CarRequesttravelautorization")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=False, related_name="CarRequestcar")
    driver = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=False, related_name="CarRequestemployee")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="CarRequestcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="CarRequestupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="CarRequestdeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.travel_autorization.purpose_of_travel}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='10-Data-Custom-CarRequest'


class PersonTraveling(models.Model):
    travel_autorization = models.ForeignKey(TravelAutorization, on_delete=models.CASCADE, null=True, blank=False, related_name="PersonTravelingtravelautorization")
    employee = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=False, related_name="PersonTravelingemployee")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="PersonTravelingcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="PersonTravelingupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="PersonTravelingdeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.travel_autorization.purpose_of_travel}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='10-Data-Custom-Person_Traveling'


class RouteTravel(models.Model):
    travel_autorization = models.ForeignKey(TravelAutorization, on_delete=models.CASCADE, null=True, blank=False, related_name="RouteTraveltravelautorization")
    munisipiu = models.ForeignKey(Munisipiu, on_delete=models.CASCADE, null=True, blank=False, verbose_name="Route", related_name="RouteTravelmunisipiu")
    deskrisaun = models.CharField(max_length=100, null=False, blank=False, verbose_name="Deskrisaun")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="RouteTravelcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="RouteTravelupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="RouteTraveldeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.travel_autorization.purpose_of_travel}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='10-Data-Custom-RouteTravel'


class AproveTravelAutorization(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=False, related_name="AproveTravelAutorizationcontract")
    travelautorization = models.ForeignKey(TravelAutorization, on_delete=models.CASCADE, null=True, blank=False, related_name="AproveTravelAutorizationmedicalexpense")
    status = models.CharField(choices=[('Review','Review'),('Acepted','Acepted'),('Rejected','Rejected')],max_length=30, null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="AproveTravelAutorizationcreatedby")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="AproveTravelAutorizationupdatedby")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="AproveTravelAutorizationdeletedby")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.status}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='1-Data-Medical-AproveTravelAutorization'