from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Team 
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    teams = Team.objects.all();
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured = True)
    all_cars = Car.objects.order_by('-created_date')
    #search_fields = Car.objects.values('model', 'city', 'year', 'body_stlye')
    model_search = Car.objects.values_list('model', flat=True).distinct();
    city_search = Car.objects.values_list('city', flat=True).distinct();
    year_search = Car.objects.values_list('year', flat=True).distinct();
    body_type_search = Car.objects.values_list('body_stlye', flat=True).distinct();
    
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        #'search_fields': search_fields,
        "model_search": model_search,
        "city_search": city_search,
        "year_search": year_search,
        "body_type_search": body_type_search,
        
        
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST["name"];
        email = request.POST["email"];
        subject = request.POST["subject"];
        phone = request.POST["phone"];
        message = request.POST["message"];
        admin_info = User.objects.get(is_superuser = True);
        admin_email = admin_info.email;
        email_subject = "You have a new message from Cargeeks regarding the " + subject + " you interested in. ";
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone ' + phone + '. Message: ' + message;
        send_mail(
            email_subject,
            message_body,
            'kongjiajun555@outlook.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, "Thanks for contacting us. We will get back to you soon.");
        return redirect('contact');
        
    return render(request, 'pages/contact.html')
