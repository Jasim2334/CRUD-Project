from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import Details
from .models import employee
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import signupForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# This function is for adding the data


def sign_up(request):
    if request.method == "POST":
        fm = signupForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Register Successfully !")
            fm.save()
    else:
        fm = signupForm()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/add/')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def add(request):
    if request.method == "POST":
        fm = Details(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            sal = fm.cleaned_data['salary']
            desg = fm.cleaned_data['designation']
            com = fm.cleaned_data['company']
            reg = employee(name=nm, salary=sal, designation=desg, company=com)
            reg.save()
            return redirect('/show')

    else:
        fm = Details()
    return render(request, 'add.html', {'form': fm, 'fname': request.user.first_name, 'lname': request.user.last_name})

# This functions is for showing the data


def show(request):
    emp = employee.objects.all()
    return render(request, 'show.html', {'e': emp})


# This is for updating the data


def user_update(request, id):
    if request.method == "POST":
        pi = employee.objects.get(pk=id)
        fm = Details(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('/show')
    else:
        pi = employee.objects.get(pk=id)
        fm = Details(instance=pi)
    return render(request, 'update.html', {'form': fm})

# This function is for deleting the data


def user_delete(request, id):
    if request.method == "POST":
        pi = employee.objects.get(pk=id)
        pi.delete()
        return redirect('/show')
