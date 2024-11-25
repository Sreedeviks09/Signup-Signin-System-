from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def IndexPage(request):
    return render(request,'index.html')


def SignUpPage(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        
        if pass1!=pass2:
             return HttpResponse("Your Password and Confirm Password are not same")
         
        else:
            Myuser = User.objects.create_user(uname,email,pass1)
            Myuser.save()
            return redirect('Signin')
        
    return render(request,'SignUp.html')


def SignInPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1= request.POST.get('pass')
        User =authenticate(request,username=username,password=pass1)
        
        if User is not None:
            login(request,User)
            return redirect('index')
        else :
            return HttpResponse("Your Username or Password is incorrect!!!")
        
    return render(request,'SignIn.html')


def Signout(request):
    logout(request)
    return render(request,'SignUp.html')