from django.shortcuts import render
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
import os

from main.models import ContactModel
from django.conf import settings


# Create your views here.
def download_cv_view(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'cv/Obidjonova_Robiya.pdf')
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Obidjonova_Robiya.pdf"'
        return response


def contactView(request):
    birth_date = date(2007, 10, 23)
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('from_email')
        subject = request.POST.get('subject')
        ContactModel.objects.create(name=name, message=message, from_email=email, subject=subject)
        message = f"I'm {name}\n{subject}\n\n{message}\n\n\nMy email: {email}"
        send_mail(
            f'MySite -> From {email}',
            message,
            '',
            ['inspiring.sunset07@gmail.com'],
            fail_silently=False
        )

    return render(request, "parts/base.html", {'birth_date': age})


def successView(request):
    return render(request, "contact.html")
