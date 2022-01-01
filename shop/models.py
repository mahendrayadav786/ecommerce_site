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
    img = models.ImageField(upload_to ="shop/images", default="")

    def __str__(self):
        return self.product_name