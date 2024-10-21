from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Hardcoded username and password check
            if username == 'user' and password == '12345':
                # Simulate successful login
                return redirect('index')  # Redirect to a success page
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'hello/login.html', {'form': form})