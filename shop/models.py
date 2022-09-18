from pickle import TRUE
from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category= models.CharField(max_length=30, default="")
    subcategory=models.CharField(max_length=30, default="")             # for superuser 
    price=models.IntegerField(default=0)
    desc= models.CharField(max_length=2000)
    pub_date = models.DateField()
    image= models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True) #implement make primary key
    name = models.CharField(max_length=50)                             #for contact.html
    email = models.CharField(max_length=30, default="")
    phone = models.CharField(max_length=300,default="")
    desc= models.CharField(max_length=2000,default="")


    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True) #implement
    items_json = models.CharField(max_length=3000,default="")
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=200)                   # for checkout.html
    phone = models.CharField(max_length=10)
    city  = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10,default="")

    def __str__(self):
       return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True) #implement
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=2000)                          # for tracker.html
    timestamp= models.DateField(auto_now_add=True) #auto now add used for user doesnt specify value automaticaly fatch default time
                                                                    

    def __str__(self):
       return self.update_desc[0:7]+"..."

