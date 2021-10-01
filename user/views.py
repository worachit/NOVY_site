from django.shortcuts import render, redirect

from .forms import userForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as buildInLogin, logout as buildInLogout
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            buildInLogin(request, user)
            return redirect('/')
        else:
            messages.info(request,"ชื่อบัญชี หรือรหัสผ่านไม่ถูกต้อง")

    return render(request, 'login.html')

def logout(request):
    buildInLogout(request)
    return redirect('/user/login')

def signup(request):
    # if request.user.is_authenticated():
    #     return redirect('/user')
    form = userForm()

    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.cleaned_data.get('username')
            new_user = authenticate(username=form.cleaned_data.get('username'),
                                    password=form.cleaned_data.get('password1'),
                                    )
            buildInLogin(request, new_user)
            
            return redirect('/')
            # messages.success(request, "สร้างบัญชีสำเร็จ โปรดเข้าสู่ระบบ")

            # return redirect('/user/login')

    context = {'form' : form}
    return render(request, 'register.html', context)