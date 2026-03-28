from django.shortcuts import render, redirect

def home(request):
    return render(request, 'reports/home.html')

def report(request):
    if request.method == 'POST':
        return render(request, 'reports/report.html', {'success': True})
    return render(request, 'reports/report.html')

def about(request):
    return render(request, 'reports/about.html')

def contact(request):
    return render(request, 'reports/contact.html')

def check_login(request):
    if request.session.get('user'):
        return redirect('report')
    else:
        return redirect('login')

def track_report(request):
    return render(request, 'reports/track_report.html')

def logout(request):
    request.session.flush()
    return redirect('home')
