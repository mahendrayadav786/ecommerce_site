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




