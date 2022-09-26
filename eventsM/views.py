from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
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
                  fail_silently=False)
    return render(request, 'eventsM/index.html', {})


class HomeView(TemplateView):

    """
    View to render homepage
    """
    template_name = 'eventsM/index.html'