from django.db import models
 
from authApp.models import UserProfile

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    image_key = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = 'product'

class Description(models.Model):
    description_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.IntegerField(default=0)
    product_number = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = 'description'

class ProductDescription(models.Model):
    product_description_id = models.AutoField(primary_key=True)
    product = models.IntegerField(default=0)
    description = models.ForeignKey(Description, on_delete=models.CASCADE, related_name='product_description')
    productproduct_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id_description')

    def __str__(self):
        return self.product_id
    
    class Meta:
        db_table = 'product_description'

class ProductUser(models.Model):
    product_user_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(default=0)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='product_user')
    productproduct_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id_user')

    def __str__(self):
        return self.product_id
    
    class Meta:
        db_table = 'product_user'
