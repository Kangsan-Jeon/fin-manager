from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.

def main(request):
    if request.method == "GET":
        return render(request, 'users/main.html')
    
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('finance:index'))
        else:
            return render(request, 'users/main.html')
