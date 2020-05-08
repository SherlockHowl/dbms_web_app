from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout

from .forms import LoginForm, RegisterForm

def home_view(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, 'hometemp/premeium_home_view.html', context)
    return render(request, 'hometemp/home_view.html', context)

def login_page_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('error')
    context = {
        'login_form': form
    }
    return render(request, 'auth/login_page.html', context)
    


User = get_user_model()
def register_page_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        'register_form': form

    }
    if(form.is_valid()):
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        #now, here if you make it (email, username, password) like this it will automatically take emails as usernames.
        print(new_user)

    return render(request, 'auth/register_page.html', context)
    
def contact_view(request):
    return render(request, 'hometemp/contact.html', {})


def logout_page_view(request):
    logout(request)
    return redirect('/')