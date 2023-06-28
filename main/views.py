from django.shortcuts import render
from datetime import date


# Create your views here.
def index_view(request):
    birth_date = date(2007, 10, 23)
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return render(request, 'parts/base.html', {'birth_date': age})

# Python, SQL

# Docker, Telegram Bot, OOP, Linux (Ubuntu), Django, FastAPI
# Postman, Twilio, Git (GitHub), HTML5, CSS3
# Bootstrap, MySQL, PostgreSQL, SQLite, Aiogram, Testing (PyTest/Unittest)

# problem solving, communication, negotiation, collaboration, adaptability