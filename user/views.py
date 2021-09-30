from django.shortcuts import render

# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login as builtInLogin, logout as builtInLogout

# Create your views here.
# def signup(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)

#         if form.is_valid():
#             user_form = form.save()
#             builtInLogin(request, user_form)
#             return redirect("/")
            
#     else:
#         form = RegistrationForm()

#         return render(request, 'register.html', {'form' : form})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'register.html')