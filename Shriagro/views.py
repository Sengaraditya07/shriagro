from django.shortcuts import render,redirect
from service.models import Product,Enquiry
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def certificates(request):
    return render(request,"certificates.html" )

def contact_view(request):
    try:
        if request.method=='POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            company = request.POST['company']
            print("hello")
            obj=Enquiry(name=name,email=email,phone=phone,message=message,company=company)
            obj.save()
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message} \nCompany:{company} \nPhone  :{phone}"
            send_mail(
            "Contact Form",
            full_message,
            'sengar.aditya07@gmail.com',
            ['sengar.adityaofficial@gmail.com'],
            fail_silently=False            
            )
            print("success...")
            return HttpResponse("Thankyou")  # You can render a success page if you like
    except Exception as e : 
            print(f"Error : {e}")
    return render(request, 'contact.html')

def products(request):
    obj=Product.objects.all()
    data={
        'prod_data':obj
    }
    return render(request,"products.html",data)
