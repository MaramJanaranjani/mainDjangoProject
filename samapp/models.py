from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length = 10, null = True, blank = True, default = None)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
class areas(models.Model):
    area = models.CharField(max_length=50)
    def __str__(self):
        return self.area

class sectors(models.Model):
    sectors = models.CharField(max_length=50)
    images = models.CharField(max_length = 50)
    def __str__(self):
        return self.sectors
class dresses(models.Model):
    dresses = models.CharField(max_length=50)
    def __str__(self):
        return self.dresses

class services(models.Model):
    service = models.CharField(max_length=50)
    def __str__(self):
        return self.service

class cities(models.Model):
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.city

class city_areamap(models.Model):
    city_id = models.ForeignKey(cities)
    area_id = models.ForeignKey(areas)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(str(self.city_id), str(self.area_id),self.latitude, self.longitude)


class laundries(models.Model):
    laundry_name = models.CharField(max_length = 20)
    city_areamapid = models.ForeignKey(city_areamap)
    sector_id = models.ForeignKey(sectors)
    phno = models.CharField(max_length = 10, null = True, blank = True, default = None)
    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.laundry_name,str(self.city_areamapid), str(self.sector_id), self.phno)

class dress_servicemap(models.Model):
    laundry_id = models.ForeignKey(laundries)
    dress_id = models.ForeignKey(dresses)
    service_id = models.ForeignKey(services)
    cost = models.CharField(max_length=50)
    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.laundry_id, str(self.dress_id), str(self.service_id), self.cost) 

class excess_cost(models.Model):
    laundry_id = models.ForeignKey(laundries)
    days = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    def __str__(self):
        return "{0}-{1}-{2}".format(self.laundry_id, self.days, self.cost)
class orders(models.Model):
    address = models.CharField(max_length=50)
    phno = models.CharField(max_length = 10, null = True, blank = True, default = None)
    date =  models.DateField(auto_now_add = True)
    time =  models.DateTimeField(default=timezone.now)
    laundry_id = models.ForeignKey(laundries)
    dress_servicemapid = models.ForeignKey(dress_servicemap)
    excess_costid = models.ForeignKey(excess_cost)
    def __str__(self):
       return "{0}-{1}-{2}-{3}-{4}-{5}-{6}".format(self.address, self.phno, self.date, self.time, self.laundry_id ,str(self.dress_servicemapid),str(self.excess_costid))
