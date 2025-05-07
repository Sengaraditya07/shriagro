from django.contrib import admin
from .models import Product,Enquiry
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('prod_head','prod_desc','prod_image','prod_benefit','prod_Shinfo','prod_nutinfo','prod_howtouse','prod_imptips')


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message','submitted_at')
