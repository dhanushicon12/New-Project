from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from users.models import UserRegistrationModel

# Create your views here.
def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'dhanush' and pswd == 'dhanush':
            return render(request, 'admins/AdminHome.html')

        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})


def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


def RegisterUsersView(request):
    data = UserRegistrationModel.objects.all()
    return render(request,'admins/viewregisterusers.html',{'data':data})

def ActivaUsers(request):
    uid = request.GET.get('uid')

    if uid:
        UserRegistrationModel.objects.filter(id=uid).update(status='activated')
        return redirect('ActivaUsers')

    data = UserRegistrationModel.objects.all()
    return render(request, 'admins/viewregisterusers.html', {'data': data})