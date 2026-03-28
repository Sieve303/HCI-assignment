from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def report(request):
    if request.method == 'POST':
        return render(request, 'report.html', {'success': True})
    return render(request, 'report.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def check_login(request):
    if request.session.get('user'):
        return redirect('report')
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        request.session['user'] = True
        return redirect('report')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        request.session['user'] = True
        return redirect('report')
    return render(request, 'signup.html')

def logout(request):
    request.session.flush()
    return redirect('home')

def track_report(request):
    return render(request, 'track_report.html')
