from django.shortcuts import render, redirect
from .forms import SignUpForm, LogInForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from . models import Record
# Create your views here.


def home(request):
    return render(request, 'project/index.html')

#
#


# SignUp User
def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    context = {'form': form}
    return render(request, 'project/signup.html', context)


# Login In
def signin(request):
    form = LogInForm()
    if request.method == 'POST':
        form = LogInForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'project/signin.html', context)


# LogOut
def logout(request):
    auth.logout(request)
    return redirect('signin')


#
#

@login_required(login_url="signin")
def dashboard(request):
    myRecords = Record.objects.all()

    context = {'records': myRecords}
    return render(request, 'project/dashboard.html', context)


@login_required(login_url="signin")
def create_record(request):
    form = CreateRecordForm()

    if request.method == 'POST':
        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

        return redirect('dashboard')

    context = {'form': form}
    return render(request, 'project/create_record.html', context)


# View Record

# Update Record
@login_required(login_url="signin")
def view_record(request, pk):
    record = Record.objects.get(id=pk)

    context = {'record': record}
    return render(request, 'project/view_record.html', context)

# Update Record


@login_required(login_url="signin")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'project/update_record.html', context)


@login_required(login_url="signin")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect('dashboard')
