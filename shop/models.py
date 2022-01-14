from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name =models.CharField(max_length = 50)
    price = models.IntegerField(default =0)
    category = models.CharField(max_length= 50, default ="")
    subcategory = models.CharField(max_length= 50, default ="")
    desc = models.CharField(max_length = 60)
    pub_date =models.DateField
    image = models.ImageField(upload_to ="shop/images", default="")

    def __str__(self):
        return self.product_name


class contact(models.Model):
        mesg_id = models.AutoField
        name = models.CharField(max_length=50)
        email = models.CharField(max_length=50)
        phone = models.IntegerField()
        desc = models.CharField(max_length=60)

        def __str__(self):
            return self.name


class Order(models.Model):
    order_id =models.AutoField(primary_key = True)
    item_json = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    zip_code = models.CharField(max_length=500)
    state = models.CharField(max_length=500)

    def __str__(self):
            return self.name

