import re
from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from .models import SubscribedUsers


def index(request):
    """Get in touch with us gmail settings"""
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'message': message
        }
        message = '''
                New message: {}
                From: {}
                '''.format(data['message'], data['email'])
        print(data)
        send_mail(f'Customer Query: { data["name"] }', data['message'],
                  data["email"], ['eventswithfinesse1@gmail.com'],
                  fail_silently=False,)
        messages.success(request, 'Contact Form sent successfully!')
    return render(request, 'eventsM/index.html', {})


class HomeView(TemplateView):

    """
    View to render homepage
    """
    template_name = 'eventsM/index.html'


def footer(request):
    """Newsletter subscribed users"""
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        name = post_data.get("name", None)
        subscribedUsers = SubscribedUsers()
        subscribedUsers.email = email
        subscribedUsers.name = name
        subscribedUsers.save()
        # send a confirmation mail
        subject = 'NewsLetter Subscription'
        message = 'Hello ' + name + ', Thanks for subscribing us.You will get \
                                       notification of latest articles posted \
                                       on our website. Please do not reply on \
                                       this email.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
        return res
    return render(request, 'footer.html')


def newslett(request):
    """Newsletters contacting users via email & name"""
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        name = post_data.get("name", None)
        subscribedUsers = SubscribedUsers()
        subscribedUsers.email = email
        subscribedUsers.name = name
        subscribedUsers.save()
        # send a confirmation mail
        subject = 'NewsLetter Subscription'
        message = ('Hello ' + name + ', Thanks for subscribing us. You will'
                   ' get notification of latest articles posted on our'
                   ' website. Please do not reply on this email.')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
        return res
    return render(request, 'index.html')


def validate_email(request):
    """Newsletter validate email, where we accept just once the email"""
    email = request.POST.get("email", None)
    if email is None:
        res = JsonResponse({'msg': 'Email is required.'})
    elif SubscribedUsers.objects.filter(email=email):
        res = JsonResponse({'msg': 'Email Address already exists'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",
                      email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        res = JsonResponse({'msg': ''})
    return res
