from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_mail_page(request):
    context={}
    if request.method == "POST":
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent sucessfully'
            
            except Exception as e:
                context['result'] = f"Error sending email: {e}"
        else:
            context['result'] = "All fields are required to fill"
    return render(request, "index.html", context)