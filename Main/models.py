from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date

# Create your models here.
class House(models.Model):
    name = models.CharField("house name", max_length=200)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    state = models.CharField("state", max_length=200, blank=True)
    suburb = models.CharField("suburb", max_length=200, blank=True)
    street = models.CharField("street", max_length=200, blank=True)
    unit_number = models.CharField("unit_number", max_length=100, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField("category name", max_length=200)
    house = models.ForeignKey(House, on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name 

class Item(models.Model):
    name =  models.CharField('Item Name', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    item_image = models.ImageField(null=True, blank=True, upload_to="images/")
    cost = models.FloatField()
    placement = models.CharField('Location', max_length=200, blank=True)
    expiry_date = models.DateField('Expiry Date') 
    last_time_used = models.DateTimeField(auto_now=True)
    account = models.URLField('associated account', blank=True)
    sold_price = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def Days_till(self):
        days_till = self.expiry_date - date.today()
        days_till_stripped = str(days_till).split(",")[0]
        return days_till_stripped

    @property
    def Is_Expired(self):
        today = date.today()
        if self.expiry_date < today:
            expired = "Yes"
        else:
            expired = "No"
        return expired

    @property
    def Near_Expiry(self):
        days_till = self.expiry_date- datetime.timedelta(days=7)
        today = date.today()
        if days_till < today:
            near = "Yes"
        else:
            near = "No"
        return near


class User(models.Model):
    first_name = models.CharField("first name", max_length=200)
    last_name = models.CharField("last name", max_length=200)
    email = models.CharField("email", max_length=100)
    items = models.ManyToManyField(Item, blank=True)
    country = models.CharField("country", max_length=200, default='Australia')
    city = models.CharField("city", max_length=200, default='Sydney')

    def __str__(self):
        return self.first_name+' ' + self.last_name

    

    
