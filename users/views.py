from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from users.forms import SignUpForm


# Create your views here.

def main(request):
    if request.method == "GET":
        return render(request, 'users/main.html')
    
    elif request.method == "POST":
        user_id = request.POST['user_id']
        password = request.POST['password']
        user = authenticate(request, user_id=user_id, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('finance:index'))
        else:
            return render(request, 'users/main.html')

def signup(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})
    
    elif request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            user_id = form.cleaned_data["user_id"]
            password = form.cleaned_data["password"]

            user = authenticate(request, user_id=user_id, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('finance:index'))
            else:
                return render(request, 'users/main.html')
        
        return render(request, 'users/main.html')
