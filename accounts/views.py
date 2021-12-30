from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == "POST":
        username = request.POST['username'];
        password = request.POST['password'];
        user = auth.authenticate(username = username, password = password);
        if user:
            auth.login(request, user);
            messages.success(request, "You have sucessfully logged in.");
            return redirect('dashboard');
        
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login');
        
        
    return render(request, 'accounts/login.html');

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname'];
        lastname = request.POST['lastname'];
        username = request.POST['username'];
        email = request.POST['email'];
        password = request.POST['password'];
        password_confirmed = request.POST['confirm_password'];
        
        if password != password_confirmed:
            messages.error(request, 'Password not matched.')
            return redirect('register');
        
        if User.objects.filter(username = username).exists():
            messages.error(request, 'User name exists.')
            return redirect('register');
        
        if User.objects.filter(email = email).exists():
            messages.error(request, 'Email exists.')
            return redirect('register');
        
        user = User.objects.create_user(first_name = firstname, last_name = lastname, email = email, username = username, password = password);
        auth.login(request, user)
        messages.success(request, 'You are now logged in.')
        return redirect('dashboard')
        user.save();
        messages.success(request, 'Signed up successfully');
        return redirect('login');
        
    
    return render(request, 'accounts/register.html');

@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by("create_date").filter(user_id = request.user.id);
    data = {
        'inquiries': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data);

def logout(request):
    if request.method == "POST":
        auth.logout(request);
        messages.success(request, "You have logged out.");
        return redirect('home');
        
        
    return redirect('home')