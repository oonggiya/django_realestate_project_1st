from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(Max_length=200)
  address = models.CharField(Max_length=200)
  city = models.CharField(Max_length=100)
  state = models.CharField(Max_length=100)
  zipcode = models.CharField(Max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bderooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  Photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  Photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', black=True)
  Photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', black=True)
  Photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', black=True)
  Photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', black=True)
  Photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', black=True)
  Photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', black=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title
