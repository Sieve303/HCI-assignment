from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        request.session['user'] = True
        return redirect('report')
    return render(request, 'users/login.html')

def signup(request):
    if request.method == 'POST':
        request.session['user'] = True
        return redirect('report')
    return render(request, 'users/signup.html')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('home')
