from django.shortcuts import render

# ---------------------------------------
# Home Page
# ---------------------------------------
def home(request):
    return render(request, 'main/home.html')

# ---------------------------------------
# User Pages
# ---------------------------------------
def login_page(request):
    return render(request, 'main/login.html')

def signup_page(request):
    return render(request, 'main/signup.html')

def user_dashboard(request):
    return render(request, 'main/user_dashboard.html')

def appointment_history(request):
    return render(request, 'main/appointment_history.html')

def book_appointment(request):
    return render(request, 'main/book_appointment.html')

# ---------------------------------------
# Astrologer Pages
# ---------------------------------------
def astrologer_profile(request):
    return render(request, 'main/astrologer_profile.html')   # 🔥 REQUIRED

def astro_login(request):
    return render(request, 'main/astro_login.html')

def astro_dashboard(request):
    return render(request, 'main/astro_dashboard.html')

def schedule_management(request):
    return render(request, 'main/schedule_management.html')

# ---------------------------------------
# Admin Pages
# ---------------------------------------
def admin_login(request):
    return render(request, 'main/admin_login.html')

def admin_dashboard(request):
    return render(request, 'main/admin_dashboard.html')