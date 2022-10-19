from django.db import models

class show(models.Model):
     full_name = models.CharField(max_length=45, default=None)


class hotel(models.Model):
    name = models.CharField(max_length=45, default=None)
    address = models.CharField(max_length=45, default=None)
    stars = models.CharField(max_length=3, default=None)
    country = models.CharField(max_length=45, default=None)
    image = models.ImageField(default=None)

class room(models.Model):
     hotel_id = models.ForeignKey(hotel, models.DO_NOTHING, default=None)
     category = models.CharField(max_length=45, default=None)
     max_count = models.IntegerField(blank=True, null=True, default=None)
     bed_type = models.CharField(max_length=45, default=None)
     price = models.IntegerField(blank=True, null=True, default=None)
     total = models.IntegerField(blank=True, null=True, default=None)




