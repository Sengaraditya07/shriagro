from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Product(models.Model):
    prod_head=models.CharField(max_length=50,default="Default Head")
    prod_image = models.FileField(upload_to='Media/')
    prod_desc=HTMLField()
    prod_benefit=HTMLField()
    prod_howtouse=HTMLField()
    prod_imptips=HTMLField()
    prod_Shinfo=HTMLField()
    prod_nutinfo=HTMLField()

    def __str__(self):
        return self.prod_head
    
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    phone=models.IntegerField(default=123)
    company=models.CharField(max_length=50,default="Shriagro")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}" 


