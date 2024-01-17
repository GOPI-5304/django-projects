from django.db import models

# Create your models here.

class product(models.Model):
    product_name=models.CharField(max_length=255)
    category=models.CharField(max_length=150)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    
    def __str__(self):
        return self.product_name
    

class feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name