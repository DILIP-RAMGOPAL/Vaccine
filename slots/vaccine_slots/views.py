from django.shortcuts import render
import requests
from django.core.mail import send_mail


def data(request):
    subject = "Vaccine Status"
    responses = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=303&date=20-04-2021')
    data = responses.json()
    a = []
    for i in data["sessions"]:
        a.append(i['block_name'])
    message = a[0]
    from_email = "dilipdrg@gmail.com"
    send_mail(subject, message, from_email, ['dilip.ramgopal.98@gmail.com'])
    return render(request, "index.html", {"data": "done"})
