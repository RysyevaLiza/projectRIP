from django.db import models

class show(models.Model):
     full_name = models.CharField(max_length=45, default=None)

class client(models.Model):
    full_name = models.CharField(max_length=45, default=None)
    number_card = models.IntegerField(blank=True, null=True,default=None)
    phone = models.CharField(max_length=11, default=None)
    email = models.EmailField(max_length=45, default=None)

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


class order(models.Model):
     hotel_id = models.ForeignKey(hotel, models.DO_NOTHING, default=None)
     room_id = models.ForeignKey(room, models.DO_NOTHING, default=None)
     client_id = models.ForeignKey(client, models.DO_NOTHING, default=None)
     check_in = models.DateTimeField(max_length=45, default=None)
     check_out = models.DateTimeField(blank=True, null=True, default=None)
     total = models.IntegerField(blank=True, null=True, default=None)

class range(models.Model):
     rangeName = models.CharField(unique=True, max_length=30, default=None)

